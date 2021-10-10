#!/usr/bin/env python3

import asyncio
import aiohttp


async def vowel_counts(one_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(one_url) as response:
            co