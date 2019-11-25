#!/usr/bin/env python3

import socket
import subprocess as sp
import datetime
import re

MOSAR2 = "192.168.1.207"
MOSAR3 = "192.168.1.120"
MOSAR4 = ""
MOSAR8 = ""
PORT = 65432
debitIPerf = "10M"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    s.connect((MOSAR2, PORT))
    #s.connect((MOSAR3, PORT))
    #s.connect((MOSAR4, PORT))
    #s.connect((MOSAR8, PORT))
sp.run(["iperf3 -c 192.168.1.1 -t 40 -b " + debitIPerf], shell = True)
iwconfig = sp.check_output(["iwconfig"], shell = True).decode("utf-8")
mcs = re.findall(r"Bit Rate=(\d+)", iwconfig)
fichierRecap = open(str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year) + "_Mosar2.txt", "a")
fichierRecap.write(debitIPerf + "\n")
fichierRecap.write(mcs[0] + "\n")
