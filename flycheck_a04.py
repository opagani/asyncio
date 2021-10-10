#!/usr/bin/env python3

import asyncio

# I'm going to write a second coroutine function


async def greet(s, n):
    for i in range(n):
        # cede control of the CPU with await in your function
        print(s)
        await asyncio.sleep(0.1)   # go to sleep -- aka give up control
    return f'Done with greet({s})'


async def main():
    # set up / schedule the tasks -- what do you want to run?
    t1 = asyncio.create_task(greet('hello', 3), name='hello-task')
    t2 = asyncio.create_task(greet('goodbye', 4), name='goodbye-task')

    # I want to say: let's wait for a bunch of them
    # tasks = [t1, t2]            # create a list of tasks
    # create a new future with these two tasks
    # results = await asyncio.gather(*tasks)

    # the above line is the same as saying
    # results = await asyncio.gather(t1, t2)

    print(results)

# how do we run it? We put it on the event loop
# I don't put main, the function, on the event loop
# rather, I put main(), the result of calling main, on the loop
print('Before')
asyncio.run(main())
print('After')
