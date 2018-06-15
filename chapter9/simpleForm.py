#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

if __name__ == '__main__':
    params = {'firstname': 'Tony', 'lastname': 'Xu'}
    r = requests.post(
        'http://pythonscraping.com/pages/files/processing.php', data=params)
    print(r.status_code)
    print(r.text)
