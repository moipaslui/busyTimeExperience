#!/usr/bin/env python3

import socket
import subprocess as sp
import datetime
import re
import time
import sys

MOSAR2 = "192.168.1.207"
MOSAR3 = "192.168.1.120"
MOSAR4 = "192.168.1.178"
MOSAR8 = "192.168.1.78"
PORT = 65432
if(len(sys.argv) == 1) :
    debitIPerf = "100M"
else :
    debitIPerf = sys.argv[1]
nombreMesure = 5
i = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
    #s.connect((MOSAR2, PORT))
    #s.connect((MOSAR3, PORT))
    #s.connect((MOSAR4, PORT))
    s.connect((MOSAR8, PORT))

while i < nombreMesure :
    if(time.localtime().tm_min % 3 == 0) :
        sp.run(["iperf3 -c 192.168.1.1 -u -M 500 -t 40 -b " + debitIPerf], shell = True)
        iwconfig = sp.check_output(["iwconfig"], shell = True).decode("utf-8")
        mcs = re.findall(r"Bit Rate=(\d+)", iwconfig)
        iPerfRecap = re.findall(r"(\d*\.?\d*)", debitIPerf) #pour avoir le débit sans le M
        fichierRecap = open("_" + str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year) + "_Mosar8.txt", "a")
        fichierRecap.write(iPerfRecap[0] + " " + mcs[0] + "\n")
        i+=1
        if(i != nombreMesure) :
            time.sleep(60)
fichierRecap.close()    
i = 0
