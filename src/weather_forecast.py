import json
import sys
import argparse
import requests
import singer
import backoff

base_url = 'http://api.openweathermap.org/data/2.5/weather'
logger = singer.get_logger()
session = requests.Session()


def parse_response(resp):
    """Parse requests response.

    `resp` will have the following format:

        {'base': 'stations',
         'clouds': {'all': 20},
         'cod': 200,
         'coord': {'lat': 46.05, 'lon': 14.51},
         'dt': 1495803600,
         'id': 3196359,
         'main': {'humidity': 37,
                  'pressure': 1018,
                  'temp': 295.7,
                  'temp_max': 296.15,
                  'temp_min': 295.15},
         'name': 'Ljubljana',
         'sys': {'country': 'SI',
                 'id': 5882,
                 'message': 0.0026,
                 'sunrise': 1495768697,
                 'sunset': 1495824027,
                 'type': 1},
         'visibility': 10000,
         'weather': [{'description': 'few clouds',
                      'icon': '02d',
                      'id': 801,
                      'main': 'Clouds'}],
         'wind': {'deg': 160, 'speed': 2.1}}

    """
    flattened = {
        'Location': resp['name'],
        'Weather': resp['weather'][-1]['description'],
        'Temperature': resp['main']['temp'],
    }
    return flattened


schema = {
    'properties': {
        'Location': {'type': 'string'},
        'Weather': {'type': 'string'},
        'Temperature': {'type': 'number'},
    },
}


def giveup(error):
    logger.error(error.response.text)
    response = error.response
    return not (response.status_code == 429 or
                response.status_code >= 500)


@backoff.on_exception(backoff.constant,
                      (requests.exceptions.RequestException),
                      jitter=backoff.random_jitter,
                      max_tries=5,
                      giveup=giveup,
                      interval=30)
def request(url, params):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response


def sync(location, appid):
    logger.info('Getting weather infromation for {} from {}.'.format(
        location, base_url))
    singer.write_schema('weather_forecast', schema, 'Location')

    try:
        response = request(base_url, {'q': location, 'appid': appid})
        payload = response.json()
        singer.write_records('weather_forecast', [parse_response(payload)])

    except requests.exceptions.RequestException as e:
        logger.fatal(
            'Error on {}; received status {}: {}'.format(
                e.request.url, e.response.status_code, e.response.text))
        sys.exit(-1)

    logger.info('Tap exiting normally')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config', help='Config file', required=False)

    args = parser.parse_args()
    if args.config:
        with open(args.config) as file:
            config = json.load(file)
    else:
        config = {}

    sync(config['location'], config['appid'])


if __name__ == '__main__':
    main()
