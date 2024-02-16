import asyncio


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection("127.0.0.1", 2500, loop=loop)

    print("Send: %r" % message)  # 연결이 되면 여기서 재개된다
    writer.write(message.encode())  # 코루틴이 아니므로 메시지 전송이 끝나야 반환된다

    data = await reader.read(100)  # 메시지 수신
    print("Received: %r" % data.decode())  # 메시지가 수신되면 여기서 재개

    print("클라이언트 소켓 닫음")
    writer.close()


message = "Hellow World!"
loop = asyncio.get_event_loop()  # 이벤트 루프 생성
loop.run_until_complete(
    tcp_echo_client(message, loop)
)  # tcp_echo_client가 종료될 때까지 이벤트 루프 실행
loop.close()
