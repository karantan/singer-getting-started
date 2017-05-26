Singer Getting Started
======================

The purpose of this project is to show how singer-io
(ref: [link](https://www.singer.io/)) works. The main singer-io getting-stated
tutorial (ref: [link](https://github.com/singer-io/getting-started))
is using target-gsheet which needs additional configuration (both on
google side and locally). This project is using target-csv
(ref: [link](https://github.com/singer-io/target-csv)) instead.

Installation
------------

Install Singer Getting Started by running:

```bash
git clone https://github.com/karantan/singer-getting-started
make
```

Read `Makefile` for additional commands.


Run
---

```bash
make my-ip
```

Open my_ip.csv file to see the results.

Now let's check how tap-fixerio + target-csv works:

```bash
make check-currency
```

Open exchange_rate.csv file to see the results.


Run weather forecast
--------------------

To run `make weather-forecast` we first need to create an account on
[openweathermap.org](openweathermap.org) to obtain API key for
`api.openweathermap.org`. Once we get it we need to update
`weather-config.json` file:

```
{
    "location": "<location e.g. `London`>",
    "appid": "<openweathermap API KEY>"
}
```

And then we can just run:

```bash
make weather-forecast
```

Open weather_forecast.csv file to see the results.


Contribute
----------

- Issue Tracker: github.com/karantan/singer-getting-started/issues
- Source Code: github.com/karantan/singer-getting-started

Support
-------

If you are having issues, please let us know.

License
-------

MIT License

Copyright (c) 2017 Gasper Vozel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
