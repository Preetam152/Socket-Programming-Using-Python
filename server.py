import socket
import time

data = {
    "SetA": [{"One": 1, "Two": 2}],
    "SetB": [{"Three": 3, "Four": 4}],
    "SetC": [{"Five": 5, "Six": 6}],
    "SetD": [{"Seven": 7, "Eight": 8}],
    "SetE": [{"Nine": 9, "Ten": 10}]
}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a = ('localhost', 12345)
s.bind(a)
s.listen(1)
print('Server listening on {}:{}'.format(*a))

while True:
    c_socket, c_address = s.accept()
    print('Accepted connection from {}:{}'.format(*c_address))
    s_data = c_socket.recv(1024).decode('utf-8')
    print('Received data from client:', s_data)
    set, k = s_data.split('-')
    if set in data:
        subset = data[set]
        s_dict = subset[0]
        if k in s_dict:
            v = s_dict[k]
            for i in range(v):
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                c_socket.send(current_time.encode('utf-8'))
                time.sleep(3)
        else:
            c_socket.send('EMPTY'.encode('utf-8'))
    else:
        c_socket.send('EMPTY'.encode('utf-8'))

    c_socket.close()



