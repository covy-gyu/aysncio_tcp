import socket
import threading

def handler(c, a):
    global connections
    while True:
        data = c.recv(1024)
        for connection in connections:
            connection.send(bytes(data)) #모든 클라이언트에게 데이터 전송
            if not data: #데이터가 없으면 소켓 제거
                connections.remove(c)
                c.close()
                break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 2500))
sock.listen(1)
connections = []

while True:
    c,a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c,a))
    cThread.daemon = True
    cThread.start()
    connections.append(c) #새로운 소켓을 소켓 리스트에 추가
    print(connections)