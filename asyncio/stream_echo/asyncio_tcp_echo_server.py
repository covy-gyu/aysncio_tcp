import asyncio


async def echo_handler(reader, writer):  # 데이터 처리 코루틴
    data = await reader.read(100)  # 데이터 수신
    message = data.decode()
    addr = writer.get_extra_info("peername")
    print("Received {!r} from {!r}".format(message, addr))

    print("Send: {!r}".format(message))
    writer.write(data)  # 수신 데이터 에코
    await writer.drain()  # 쓰기 가능해질 때까지 대기

    print("클라이언트 소켓 닫음")
    writer.close()


loop = asyncio.get_event_loop()  # 현재 이벤트 루프를 가져온다
server_coro = asyncio.start_server(
    echo_handler, "localhost", 2500, loop=loop
)  # echo)handler에게 reader, writer를 넘겨준다
remote = loop.run_until_complete(
    server_coro
)  # 클라이언트의 연결 요청을 계속 서비스한다

# Ctrl+C를 눌러 중단할 때까지 서비스가 계속된다
print("Serving on {}".format(remote.sockets[0].getsockname()))
try:
    loop.run_forever()  # stop()을 호출할 떄까지 루프 실행
except KeyboardInterrupt:
    pass

# 서버 객체를 닫는다
remote.close()
loop.run_until_complete(remote.wait_closed())
loop.close()
