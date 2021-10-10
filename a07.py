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
        await asyncio.sleep(0.1)
        output *= i
    return output


async def main():
    t1 = asyncio.create_task(sumto(5))
    t2 = asyncio.create_task(factorial(5))

    results = await asyncio.gather(t1, t2)
    print(results)

asyncio.run(main())
