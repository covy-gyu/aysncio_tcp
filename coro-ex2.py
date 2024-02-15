# python>=3.7

import asyncio
import time


async def say(msg, w_time):
    await asyncio.sleep(w_time)
    print(msg)


loop = asyncio.get_event_loop()
print(f"시작 {time.strftime('%X')}")
task1 = loop.create_task(say("첫 인사", 2))
task2 = loop.create_task(say("둘 인사", 3))

loop.run_until_complete(task1)
loop.run_until_complete(task2)
print(f"끝 {time.strftime('%X')}")

loop.close()
