#!/usr/bin/env python3

import asyncio

async def hello():
    print('Hello from before !')

async def main():
    await hello()