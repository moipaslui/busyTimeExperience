#!/usr/bin/env python3

import socket
import subprocess as sp

MOSAR2 = "192.168.1.207"
MOSAR3 = "192.168.1.120"
MOSAR4 = ""
MOSAR8 = ""
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    #s.connect((MOSAR2, PORT))
    s.connect((MOSAR3, PORT))
    #s.connect((MOSAR4, PORT))
    #s.connect((MOSAR8, PORT))
sp.run(["iperf3 -c 192.168.1.1 -t 40"], shell = True)