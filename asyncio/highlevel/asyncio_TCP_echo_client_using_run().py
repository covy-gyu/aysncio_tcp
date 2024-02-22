import asyncio


class EchoClientProtocol(asyncio.Protocol):  # protocol 클래스
    def __init__(self, message, on_con_lost, loop):
        self.message = message
        self.loop = loop  # 이벤트 루프
        self.on_con_lost = on_con_lost  # future 객체

    def connection_made(self, transport):
        transport.write(self.message.encode())  # 메시지 전송
        print(f"Data sent: {self.message}")

    def data_received(self, data):
        print(f"Data received: {data.decode()}")

    def connection_lost(self, exc):
        print(f"The server closed the connection")
        self.on_con_lost.set_result(True)  # 연결이 종료되면 future 결과를 True로 설정


async def main():
    # 저수준 API를 사용하기 위해 현재 이벤트 루프를 가져온다
    loop = asyncio.get_running_loop()

    on_con_lost = loop.create_future()  # 이벤트 루프에 연결되는 future 생성
    message = "hello world!"

    transport, protocol = await loop.create_connection(
        lambda: EchoClientProtocol(message, on_con_lost, loop), "127.0.0.1", 2500
    )

    # protocol이 연결 종료를 알릴 때까지 대기한 후에 연결을 닫는다
    try:
        await on_con_lost  # future 객체 작성
    finally:
        transport.close()


asyncio.run(main())
