#!/usr/bin/env python3

import asyncio


async def hello():
    print('Hello from before sleeping!')
    asyncio.sleep(1)
    print('Hello from after sleeping!')


async def main():
    await hello()

asyncio.run(main())
