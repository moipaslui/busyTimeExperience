#!/usr/bin/env python3

from calculateBusyTime import calculeBusyTime
import socket
import subprocess as sp
import time
import datetime

HOST = "192.168.1.78"
PORT = 65433        # Port to listen on (non-privileged ports are > 1023)
INTERFACE = "wlan0"
TEMPSMESURE = 20

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	while True :
		print("Le serveur écoute : \n")
		s.listen()
		conn, addr = s.accept()
		with conn:
			sp.run(["sudo ifconfig " + INTERFACE + " down"], shell = True)
			sp.run(["sudo iwconfig " + INTERFACE + " mode monitor"], shell = True)
			sp.run(["sudo rfkill unblock wlan"], shell = True)			
			sp.run(["sudo ifconfig " + INTERFACE + " up"], shell = True)
			sp.run(["sudo iwconfig " + INTERFACE + " channel 1"], shell = True)
			time.sleep(5) #il faut sleep suffisamment le temps que l'iperf se déclenche mais pas trop pour ne pas aller à la fin de l'iperf
			busyTimeTotal = calculeBusyTime(INTERFACE, TEMPSMESURE)
			time.sleep(20) #on sleep suffisamment longtemps pour attendre la fin de l'iperf
			busyTimeAmbiant = calculeBusyTime(INTERFACE, TEMPSMESURE)
			debitIPerf = recv(2048)
			fichierRecap = open(str(datetime.day) + "/" + str(datetime.month) + "/" + str(datetime.year) + "-Mosar8-" + debitIPerf, "a")
			fichierRecap.write(busyTimeTotal + "\n")
			fichierRecap.write(busyTimeAmbiant + "\n")

