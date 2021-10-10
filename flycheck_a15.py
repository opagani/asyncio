#!/usr/bin/env python3

import asyncio


# Pig Latin
def plsentence(s):
    output = []
    for one_word in s.split():
        if one_word[0] in 'aeiou':
            output.append(one_word + 'way')
        else:
            output.append(one_word[1:] + one_word[0] + 'ay')
    return ' '.join(output)


async def handle_client(reader, writer):
    print(f'Task {asyncio.current_task()}, reader ID {id(reader)}')

    while True:

        # the coroutine is run when we get a new connection
        # read data from the client (i.e., read from my "reader" socket)
        s = (await reader.read(255)).decode('utf8')

        print(f's = {s}')

        # decide what to do with the data I got
        # if it's an empty string, then end the connection
        if not s.strip():
            print('\tEnding connection')
            break

        response = plsentence(s.strip()) + '\n'
        writer.write(response.encode('utf8'))

        # send a response to the writer socket
        await writer.drain()

    # close the writer and be done
    writer.close()


async def main():
    # what coroutine do we want to use in a task when someone connects to us?
    server = await asyncio.start_server(handle_client, 'localhost', 6789)
    async with server:
        await server.serve_forever()

asyncio.run(main())
