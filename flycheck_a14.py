#!/usr/bin/env python3

import time
import asyncio
import aiohttp
from collections import defaultdict

counts = defaultdict(int)


async def vowel_counts(one_url):
    print(one_url)
    async with aiohttp.ClientSession() as session:
        async with session.get(one_url) as response:
            content = await response.text()
            for one_character in content:
                if one_character.lower() in 'aeiou':
                    counts[one_url] += 1

    print(f'\tDone with {one_url}')


async def main():
    start_time = time.perf_counter()

    tasks = []
    for one_url in ['https://lerner.co.il',
                    'https://python.org/',
                    'https://nytimes.com',
                    'https://postgresql.org']:
        t = asyncio.make_task(vowel_counts(one_url))

        await vowel_counts(one_url)

    end_time = time.perf_counter()

    print(f'Total time = {end_time - start_time}')


asyncio.run(main())
print(counts)
