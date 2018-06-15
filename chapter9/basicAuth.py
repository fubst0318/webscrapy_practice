#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    auth = HTTPBasicAuth('tony', 'password')
    r = requests.post(
        'http://pythonscraping.com/pages/auth/login.php', auth=auth)
    print(r.text)
