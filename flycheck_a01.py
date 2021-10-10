#!/usr/bin/env python3

import asyncio

# simplest possible asyncio program

# this is a coroutine!


async def main():
    print('Hello, world!')

print(main)


# how do we run it? We put it on the event loop
# I don't put main, the function, on the event loop
# rather, I put main(), the result of calling main, on the loop
asyncio.run(main())
