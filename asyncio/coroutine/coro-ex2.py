# python>=3.7

import asyncio
import time


async def say_after(w_time, msg):
    await asyncio.sleep(w_time)
    print(msg)


async def main():
    task1 = asyncio.create_task(say_after(1, "Hello"))
    task2 = asyncio.create_task(say_after(2, "World"))

    print(f"시작 {time.strftime('%X')}")

    await task1
    await task2

    print(f"끝 {time.strftime('%X')}")


asyncio.run(main())
