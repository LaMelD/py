# -*- coding: utf-8 -*-
import socket 
import time

HOST = '127.0.0.1'
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((HOST, PORT)) 
    s.sendall(b'hello, world') 
    data = s.recv(1024) 
    print('received', repr(data))
    time.sleep(2)