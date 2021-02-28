#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"

def get_soup(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)

    return bs(html.content, "html.parser")

def get_all_tables(soup):
    return soup.find_all("table")


def get_table_headers(table):
    headers = []
    for th in table.find("tr").find_all("th"):
        headers.append(th.text.strip())
    return headers

def get_table_rows(table):
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        tds = tr.find_all("td")
        if len(tds) == 0:
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)
    return rows

def save_as_csv(table_name, headers, rows):
    pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv")

def main(url):
    soup = get_soup(url)
    tables = get_all_tables(soup)
    print(f"[+] Found a total of {len(tables)} tables.")
    for i, table in enumerate(tables, start=1):
        headers = get_table_headers(table)
        rows = get_table_rows(table)
        table_name = f"table-{i}"
        print(f"[+] Saving {table_name}")
        save_as_csv(table_name, headers, rows)

if __name__ == "__main__":
    import sys
    try:
        url = sys.argv[1]
    except IndexError:
        print("Please specify a URL.\nUsage: python html_table_extractor.py [URL]")
        exit(1)
    main(url)
