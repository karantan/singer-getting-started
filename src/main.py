from datetime import datetime
from datetime import timezone

import singer
import urllib.request

now = datetime.now(timezone.utc).isoformat()
schema = {
    'properties':   {
        'ip': {'type': 'string'},
        'timestamp': {'type': 'string', 'format': 'date-time'},
    },
}

with urllib.request.urlopen('http://icanhazip.com') as response:
    ip = response.read().decode('utf-8').strip()
    singer.write_schema('my_ip', schema, 'timestamp')
    singer.write_records('my_ip', [{'timestamp': now, 'ip': ip}])
