#!/usr/bin/env python3

import asyncio

# I'm going to write a second coroutine function
async def 




async def main():
    print('Hello, world!')

# how do we run it? We put it on the event loop
# I don't put main, the function, on the event loop
# rather, I put main(), the result of calling main, on the loop
print('Before')
asyncio.run(main())
print('After')
