#!/usr/bin/env python3

import asyncio


async def sumto(n):
    total = 0
    for i in range(n+1):
        print(f'sumto, {i=}')
        await asyncio.sleep(0.1)
        total += i
    return total


async def factorial(n):
    output = 1
    for i in range(1, n+1):
        print(f'factorial, {i=}')
        await asyncio.sleep(0.5)
        output *= i
    return output


# get the event loop
# you can call this method however many times you want
# the loop is a singleton -- you'll get the same one
loop = asyncio.get_event_loop()

# create my tasks
t1 = loop.create_task(sumto(5))
t2 = loop.create_task(factorial(15))

# get a future describing all of the tasks
group = asyncio.gather(t1, t2)
loop.run_until_complete(group)
