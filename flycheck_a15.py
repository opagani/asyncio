#!/usr/bin/env python3

import asyncio


async def handle_client(reader, writer):
    print(f'Task {asyncio.current_task()}, reader ID {id(reader)}')

    # the coroutine is run when we get a new connection
    # read data from the client (i.e., read from my "reader" socket)


    # decide what to do with the data I got
    # send a response to the writer socket
    # close the writer and be done


async def main():
    # what coroutine do we want to use in a task when someone connects to us?
    server = await asyncio.start_server(handle_client, 'localhost', 6789)
    async with server:
        await server.serve_forever()

asyncio.run(main())
