import concurrent.futures as cf
from socket import *

#메시지를 수신하여 출력하고 다시 전송한다
def receive_message(sock, address):
    while True:
        r_msg = sock.recv(1024)
        if not r_msg:
            break
        sock.sendall(r_msg)
        print("전송 메시지: ",r_msg.decode())
    sock.close()
    
s_sock = socket(AF_INET, SOCK_STREAM)
s_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s_sock.bind(('',2500))
s_sock.listen(5)
print(f"{s_sock.getsockname()}에서 연결 대기 중")

#스레드를 생성하고 함수를 등록한다
with cf.ThreadPoolExecutor(max_workers=10) as th:
    try:
        while True: #다중 접속을 받는다
            c_sock, addr = s_sock.accept()
            print(f"{addr}에서 연결")
            th.submit(receive_message, c_sock, addr)
    except: #예외가 발생하면 다시 시도한다
        pass 
    finally:
        s_sock.close()
        