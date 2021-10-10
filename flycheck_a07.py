#!/usr/bin/env python3

import asyncio

async def sumto(n):
    total = 0
    for i in range(n):
        total += i
    return total

async def factorial(n):
    output = 1
    for i in range(1,n):
        output *= i
    return output

async def main():
    t1 = asyncio.create_task(sumto(5))
    t2 = asyncio.create_task(factorial(5))
    
        