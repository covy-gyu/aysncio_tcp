import asyncio


class EchoServerProtocol(asyncio.Protocol):  # protocol 클래스
    def connection_made(self, transport):
        peername = transport.get_extra_info("peername")
        print(f"Connection from {peername}")
        self.transport = transport  # 연결이 되면 연결 객체를 지정

    def data_received(self, data):
        message = data.decode()
        print(f"Data received: {message}")

        print(f"Send: {message}")
        self.transport.write(data)  # 데이터 통신

        print("Close the client socket")
        self.transport.close()  # 한 번만 서비스할 때


async def main():
    # 저수준 API를 사용하기 위해 현재 이벤트 루프를 가져온다
    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: EchoServerProtocol(), "127.0.0.1", 2500
    )  # 서버 실행 예약

    async with server:  # 서버 무한 실행
        await server.serve_forever()


asyncio.run(main())
