import socket
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
iv = get_random_bytes(16)

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_address = ('localhost', 12345)
c_socket.connect(s_address)
data = "SetA-Two"
cipher = AES.new(key, AES.MODE_CBC, iv)
encrypt_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
c_socket.send(encrypt_data)
# c_socket.send(data.encode('utf-8'))

while True:
    encrypt_resp = c_socket.recv(1024)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypt_resp = unpad(cipher.decrypt(encrypt_resp), AES.block_size).decode('utf-8')
    if decrypt_resp == 'EMPTY':
        print("Empty")
        break
    print(decrypt_resp)
    # resp = c_socket.recv(1024).decode('utf-8')
    # if resp == 'EMPTY':
    #     print('EMPTY')
    #     break
    # print(resp)

c_socket.close()
