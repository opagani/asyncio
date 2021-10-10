#!/usr/bin/env python3

import asyncio


async def hello():
    print('Hello from before sleeping!')
    await asyncio.sleep(1)
    print('Hello from after sleeping!')


def threadish():
    print('Hello from threadish!')
    return 12345


async def main():
    threadish()
    await hello()
    long_running_thread()

asyncio.run(main())
