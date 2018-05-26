#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import json
from urllib.request import urlopen


def getCountry(ipAddress):
    response = urlopen('http://freegeoip.net/json/' +
                       ipAddress).read().decode('utf-8')
    responsejson = json.loads(response)
    return responsejson.get('country_code')


if __name__ == '__main__':
    print(getCountry('50.78.253.58'))
