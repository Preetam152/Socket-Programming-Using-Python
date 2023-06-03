import socket


c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_address = ('localhost', 12345)
c_socket.connect(s_address)
data = "SetA-Two"
c_socket.send(data.encode('utf-8'))

while True:
    resp = c_socket.recv(1024).decode('utf-8')
    if resp == 'EMPTY':
        print('EMPTY')
        break
    print(resp)

c_socket.close()








