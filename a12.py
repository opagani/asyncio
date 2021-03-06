#!/usr/bin/env python3

# instead of requests, we can use a few different options
# one option: httpx, a new-ish library (tries to be compatible with requests)
# my option: aiohttp (tries to be compatiable with the asyncio style of doing things)

import asyncio
import aiohttp
import time


sites = {}


async def get_one_site(one_url):
    print(f'Getting {one_url}')

    async with aiohttp.ClientSession() as session:   # session = aiohttp.ClientSession()
        # session.__aenter__  -- asyncio enter

        # response = session.get(one_url)
        async with session.get(one_url) as response:
            content = await response.text()
            sites[one_url] = len(content)
    print(f'\tFinished with {one_url}; sites = {sites}')


async def main():
    start_time = time.perf_counter()

    tasks = []
    for one_url in ['https://lerner.co.il',
                    'https://python.org/',
                    'https://nytimes.com',
                    'https://washingtonpost.com',
                    'https://postgresql.org']:
        t = asyncio.create_task(get_one_site(one_url))
        tasks.append(t)

    # wait for all of the tasks in the "tasks" list to finish
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()

    print(f'Total time = {end_time - start_time}')


asyncio.run(main())
print(sites)
