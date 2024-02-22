# python<=3.7

import asyncio
import time


async def say(msg, w_time):
    await asyncio.sleep(w_time)
    print(msg)


async def stop_after(loop, w_time):
    await asyncio.sleep(w_time)
    loop.stop()


loop = asyncio.get_event_loop()

loop.create_task(say("first msg", 2))
loop.create_task(say("second msg", 1))
loop.create_task(say("third msg", 4))
loop.create_task(stop_after(loop, 3))

loop.run_forever()
loop.close()
