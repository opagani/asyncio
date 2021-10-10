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
    await hello()
    loop = asyncio.get_running_loop()
    loop.run_in_executor

    threadish()

asyncio.run(main())
