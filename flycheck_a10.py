#!/usr/bin/env python3

import asyncio
import requests


sites = {}


async def get_one_site(one_url):
    result = requests.get(one_url)
    sites[one_url] = len(result.content())


async def main():
    for one_url in ['https://lerner.co.il',
                    'https://python.org/',
                    'https://nytimes.com',
                    'https://washingtonpost.com',
                    'https://postgresql.org']:
        await get_one_site(one_url)



asyncio.run(main())
