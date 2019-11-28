#!/usr/bin/env python3

from calculateBusyTime import calculeBusyTime
import socket
import subprocess as sp
import time
import datetime

HOST = "192.168.1.207"
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
INTERFACE = "wlan0"
TEMPSMESURE = 20
nombreMesure = 5
i = 0

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
			while i < nombreMesure :
				if(time.localtime().tm_min % 3 == 0) : #on sychronise le client et le serveur
					time.sleep(5) #il faut sleep suffisamment le temps que l'iperf se déclenche mais pas trop pour ne pas aller à la fin de l'iperf
					print("debutBusyTime")					
					busyTimeTotal = calculeBusyTime(INTERFACE, TEMPSMESURE)
					time.sleep(20) #on sleep suffisamment longtemps pour attendre la fin de l'iperf
					print("debutAmbiant")
					busyTimeAmbiant = calculeBusyTime(INTERFACE, TEMPSMESURE)
					fichierRecap = open(str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(datetime.date.today().year) + "_Mosar2.txt", "a")
					fichierRecap.write(str(busyTimeTotal) + "\n")
					fichierRecap.write(str(busyTimeAmbiant) + "\n")
					i+=1
			fichierRecap.close()
			i = 0

