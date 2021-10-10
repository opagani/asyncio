#!/usr/bin/env python3

import asyncio
import aiohttp
from collections import defaultdict

counts = {}


async def vowel_counts(one_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(one_url) as response:
            content = await response.text()
            total = 0
            for one_character in content:
                if one_character.lower() in 'aeiou':
                    counts[one_url] += 1