#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from lxml.html import fromstring
import requests
from itertools import cycle
import traceback

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)

    return proxies

proxies = get_proxies()
proxy_pool = cycle(proxies)

for i in range(1,5):
    proxy = next(proxy_pool)
    ip = proxy
    stripped = proxy.split(':', 1)[0]
    url = f'https://ipapi.co/{stripped}/json/'
    print(url)
    try:
        response = requests.get(url,proxies={"http": f'http://{proxy}', "https": f'http://{proxy}'})
        print(response.json())
    except:
        print("Skipping. Connnection error")