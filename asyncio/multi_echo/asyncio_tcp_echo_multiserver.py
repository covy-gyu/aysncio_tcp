# start_server()를 이용한 멀티유저 에코 서버
# Dummy_TCP_client.py

import asyncio


async def echo_handler(reader, writer):
    while True:
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info("peername")
        print("Received %r from %r" % (message, addr))

        print("Send: %r" % message)
        writer.write(data)
        await writer.drain()


loop = asyncio.get_event_loop()
server_coro = asyncio.start_server(echo_handler, "127.0.0.1", 2500, loop=loop)
server = loop.run_until_complete(server_coro)  # 서버를 루프에 실행 예약

# Serve requests until Ctrl+C is pressed
print("Serving on {}".format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
