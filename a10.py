#!/usr/bin/env python3

import asyncio
import requests
import time


sites = {}


async def get_one_site(one_url):
    print(one_url)
    result = requests.get(one_url)
    sites[one_url] = len(result.content)


async def main():
    start_time = time.perf_counter()

    for one_url in ['https://lerner.co.il',
                    'https://python.org/',
                    'https://nytimes.com',
                    'https://washingtonpost.com',
                    'https://postgresql.org']:
        await get_one_site(one_url)
    end_time = time.perf_counter()

    print(f'Total time = {end_time - start_time}')


asyncio.run(main())
print(sites)
