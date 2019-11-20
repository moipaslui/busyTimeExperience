#!/usr/bin/env python3

from calculateBusyTime import calculeBusyTime
import socket
import subprocess as sp
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
INTERFACE = "wlan0"
TEMPSMESURE = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        # while True:
        sp.run(["nmcli nm wifi off"], shell = True) #setup du Mosar en mode monitor
        sp.run(["sudo ifconfig " + INTERFACE + " down"], shell = True)
        sp.run(["sudo iwconfig " + INTERFACE + " mode monitor"], shell = True)
        sp.run(["sudo ifconfig " + INTERFACE + " up"], shell = True)
        sp.run(["sudo iwconfig " + INTERFACE + " channel 1"], shell = True)
        time.sleep(30) #il faut sleep suffisamment le temps que l'iperf se déclenche mais pas trop pour ne pas aller à la fin de l'iperf
        calculeBusyTime("busyTimeTotal.txt", INTERFACE, TEMPSMESURE)
        time.sleep(30) #on sleep suffisamment longtemps pour attendre la fin de l'iperf
        calculeBusyTime("busyTimeAmbiant.txt", INTERFACE, TEMPSMESURE)
        sp.run(["nmcli nm wifi on"], shell = True)
        
