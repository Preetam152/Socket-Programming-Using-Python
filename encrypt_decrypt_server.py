import socket
import time
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

data = {
    "SetA": [{"One": 1, "Two": 2}],
    "SetB": [{"Three": 3, "Four": 4}],
    "SetC": [{"Five": 5, "Six": 6}],
    "SetD": [{"Seven": 7, "Eight": 8}],
    "SetE": [{"Nine": 9, "Ten": 10}]
}

key = get_random_bytes(16)
iv = get_random_bytes(16)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a = ('localhost', 12345)
s.bind(a)
s.listen(1)
print('Server name is {}:{}'.format(*a))

while True:
    c_socket, c_address = s.accept()
    print('Accepted connection from {}:{}'.format(*c_address))
    encrypt_data = c_socket.recv(1024)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypt_data = unpad(cipher.decrypt(encrypt_data), AES.block_size).decode('utf-8')
    print('Decrypted data from client:', decrypt_data)
    # s_data = c_socket.recv(1024).decode('utf-8')
    # print('Received data from client:', s_data)
    set, k = decrypt_data.split('-')
    if set in data:
        subset = data[set]
        s_dict = subset[0]
        if k in s_dict:
            v = s_dict[k]
            for i in range(v):
                current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                resp = pad(current_time.encode('utf-8'), AES.block_size)
                cipher = AES.new(key, AES.MODE_CBC, iv)
                encrypt_resp = cipher.encrypt(resp)
                c_socket.send(encrypt_resp)
                time.sleep(1)
        else:
            resp = pad('EMPTY'.encode('utf-8'), AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            encrypt_resp = cipher.encrypt(resp)
            c_socket.send(encrypt_resp)
            # c_socket.send('EMPTY'.encode('utf-8'))
    else:
        resp = pad('EMPTY'.encode('utf-8'), AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypt_resp = cipher.encrypt(resp)
        c_socket.send(encrypt_resp)
        # c_socket.send('EMPTY'.encode('utf-8'))

    c_socket.close()