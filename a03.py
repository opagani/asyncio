#!/usr/bin/env python3

import asyncio

# I'm going to write a second coroutine function


async def greet(s, n):
    for i in range(n):
        # cede control of the CPU with await in your function
        print(s)
        await asyncio.sleep(0.1)   # go to sleep -- aka give up control


async def main():
    # set up / schedule the tasks -- what do you want to run?
    t1 = asyncio.create_task(greet('hello', 3))
    t2 = asyncio.create_task(greet('goodbye', 4))

    # wait for t1 and t2 to finish, then let main die
    # if I use this, then main will exit after t1 and t2 are both done
    values = await t1, t2

    # alternatively, we can sleep for a certain amount of time
    # if I use this, then main will exit after 5 seconds, hopefully enough for t1+t2 to do their thing
    # asyncio.sleep(5)


# how do we run it? We put it on the event loop
# I don't put main, the function, on the event loop
# rather, I put main(), the result of calling main, on the loop
print('Before')
asyncio.run(main())
print('After')
