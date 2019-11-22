import subprocess as sp
import time
import re

def calculeBusyTime(nomInterface, tempsMesure) :
	nombresInterface = re.findall(r"\d+", nomInterface) #on calcule le nombres de chiffres dans l'interface pour pouvoir les passer dans le deuxième regex

	sp.check_output("iw dev " + nomInterface + " survey dump", shell=True).decode("utf-8") #premier survey dump pour reset les chiffres du busy time

	time.sleep(tempsMesure) #sleep pour avoir la durée voulue de la mesure

	resultatDump = sp.check_output("iw dev " + nomInterface + " survey dump", shell=True).decode("utf-8") #deuxième survey dump sur lequel on va prélever les temps
	nombres = re.findall(r"\d+", resultatDump) #regex qui récupère tous les nombres du résultat du survey dump

	tempsActif = int(nombres[len(nombresInterface) + 1]) #récupération du temps actif et busy dans le tableau de tous les nombres du survey dump
	tempsBusy = int(nombres[len(nombresInterface) + 2]) 

	pourcentageBusy = ((tempsBusy/tempsActif)*100) #calcul du pourcentage de busy time

	return(pourcentageBusy)