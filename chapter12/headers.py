#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }

    session = requests.Session()
    req = session.get(
        'https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending', headers=headers)

    bsObj = BeautifulSoup(req.text, 'html.parser')
    print(bsObj.find('table', {'class': 'table-striped'}).get_text())
