#!/usr/bin/env python3

import asyncio

# I'm going to write a second coroutine function


async def greet(s, n):
    try:
        for i in range(n):
            # cede control of the CPU with await in your function
            print(s)
            await asyncio.sleep(.3)  # wait for 3 seconds -- a long time!
        return f'Done with greet({s})'
    except asyncio.CancelledError as e:
        print(f'Canceled task {asyncio.current_task()}: {e}')


async def main():
    # set up / schedule the tasks -- what do you want to run?
    t1 = asyncio.create_task(greet('hello', 3), name='hello-task')
    t2 = asyncio.create_task(greet('goodbye', 4), name='goodbye-task')

    # get one future from t1+t2, and call it tasks
    tasks = asyncio.gather(t1, t2)

    # wait_for tasks to finish, but only give it 4 seconds
    # any longer, and we'll get  an asyncio.TimeoutError exception
    results = await asyncio.wait_for(tasks, 4)

    print(results)

# how do we run it? We put it on the event loop
# I don't put main, the function, on the event loop
# rather, I put main(), the result of calling main, on the loop
print('Before')
asyncio.run(main())
print('After')
