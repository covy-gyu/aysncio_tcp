import sys
import random
import socket
import json

# 서버의 IP 주소와 포트 번호
SERVER_IP = 'localhost'
SERVER_PORT = 2500

# 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 소켓을 서버에 연결
    sock.connect((SERVER_IP, SERVER_PORT))
    print('서버에 연결되었습니다.')
except socket.error as e:
    print('서버 연결 실패:', e)
    sys.exit()

converData = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# while True:
for i in range(1000):
    # converData.pop(0)
    # converData.append(random.randint(0,255))
    # print(converData)
    
    # data_dict = {
    #     'Group_ID': converData[0] + 1,
    #     'Receiver_Num': converData[1],
    #     'Sensor_0_type': converData[2],
    #     'Sensor_0_value': (converData[4] << 8) + converData[3],
    #     'Sensor_1_type': converData[5],
    #     'Sensor_1_value': (converData[7] << 8) + converData[6],
    #     'Sensor_2_type': converData[8],
    #     'Sensor_2_value': (converData[10] << 8) + converData[9],
    #     'EOF': (converData[14] << 24) + (converData[13] << 16) + (converData[12] << 8) + converData[11]
    # }
    json_data = json.dumps(converData)
    
    
    # 데이터를 서버로 전송
    try:
        sock.send(json_data.encode())
        print({i},' 데이터를 서버로 전송했습니다.')
    except socket.error as e:
        print('데이터 전송 실패:', e)
        sys.exit()

    # converData.clear()

