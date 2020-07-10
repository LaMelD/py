# -*- coding: utf-8 -*-
import socket

# simple-echo-server
def serve(host='0.0.0.0', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print('connected by', addr)
                if conn.recv(1024):
                    conn.sendall(b'hello python!!')

if __name__ == '__main__':
    serve()