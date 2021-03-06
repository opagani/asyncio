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
    result = loop.run_in_executor(None, threadish)
    loop = asyncio.get_running_loop()
    await hello()

    # pass the function, *without* calling it!
    print(f'{result=}')

asyncio.run(main())
