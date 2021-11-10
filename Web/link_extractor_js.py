#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from requests_html import HTMLSession
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
RESET = colorama.Fore.RESET

internal_urls = set()
external_urls = set()

total_urls_visited = 0


def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    urls = set()
    domain_name = urlparse(url).netloc
    session = HTMLSession()
    response = session.get(url)
    try:
        response.html.render()
    except:
        pass
    soup = BeautifulSoup(response.html.html, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if href in internal_urls:
            continue
        if domain_name not in href:
            if href not in external_urls:
                print(f"{GRAY}[!] External link: {href}{RESET}")
                external_urls.add(href)
            continue
        print(f"{GREEN}[*] Internal link: {href}{RESET}")
        urls.add(href)
        internal_urls.add(href)
    return urls

def crawl(url, max_urls=50):
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Link Extractor Tool with Python")
    parser.add_argument("url", help="The URL to extract links from.")
    parser.add_argument("-m", "--max-urls", help="Number of max URLs to crawl, default is 30.", default=30, type=int)
    
    args = parser.parse_args()
    url = args.url
    max_urls = args.max_urls

    crawl(url, max_urls=max_urls)

    print("[+] Total Internal links:", len(internal_urls))
    print("[+] Total External links:", len(external_urls))
    print("[+] Total URLs:", len(external_urls) + len(internal_urls))

    domain_name = urlparse(url).netloc

    with open(f"{domain_name}_internal_links.txt", "w") as f:
        for internal_link in internal_urls:
            print(internal_link.strip(), file=f)

    with open(f"{domain_name}_external_links.txt", "w") as f:
        for external_link in external_urls:
            print(external_link.strip(), file=f)