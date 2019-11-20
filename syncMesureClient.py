#!/usr/bin/env python3

import socket

HOST1 = "192.168.1.126"
HOST2 = ""
HOST3 = ""
HOST4 = ""
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.connect((HOST1, PORT))
    s.connect((HOST2, PORT))
    s.connect((HOST3, PORT))
    s.connect((HOST4, PORT))