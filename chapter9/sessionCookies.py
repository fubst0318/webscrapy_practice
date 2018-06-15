#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

if __name__ == '__main__':
    session = requests.Session()

    params = {'username': 'Tony', 'password': 'password'}
    s = session.post(
        'http://pythonscraping.com/pages/cookies/welcome.php', params)
    print('Cookie is set to:')
    print(s.cookies.get_dict())
    print('------------')
    print('Going to profile page...')
    s = session.get('http://pythonscraping.com/pages/cookies/profile.php')
    print(s.text)
