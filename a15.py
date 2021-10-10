#!/usr/bin/env python3

import asyncio


async def handle_client(reader, writer):


async def main():
    # what coroutine do we want to use in a task when someone connects to us?
    server = await asyncio.start_server(handle_client, 'localhost', 6789)
    async with server:
        await server.serve_forever()

asyncio.run(main())
