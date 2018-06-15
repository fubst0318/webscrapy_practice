#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

if __name__ == '__main__':
    files = {'uploadFile': open('../Python-logo.png', 'rb')}
    r = requests.post(
        'http://pythonscraping.com/pages/files/processing2.php', files=files)
    print(r.status_code)
    print(r.text)
