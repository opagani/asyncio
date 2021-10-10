#!/usr/bin/env python3

import asyncio

# simplest possible asyncio program

# this is a coroutine!


async def main():
    print('Hello, world!')

print(main)


# how do we run it? We put it on the event loop
asyncio.run(main())
