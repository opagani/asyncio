#!/usr/bin/env python3

import asyncio
import requests


sites = {}


async def main():
    for one_url in ['https://lerner.co.il',
                    'https://python.org/',
                    'https://nytimes.com',
                    'https://washingtonpost.com',
                    'https://postgresql.org']:
        result = requests.get(one_url)
        sites[one_url] = len(result.content())
