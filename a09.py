#!/usr/bin/env python3

import asyncio


async def hello():
    print('Hello from before sleeping!')
    await asyncio.sleep(1)
    print('Hello from after sleeping!')


def long_running_thread():
    print('Hello from the long-running thread!')
    return 12345


async def main():
    await hello()

asyncio.run(main())
