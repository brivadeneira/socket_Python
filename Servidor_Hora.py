#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Servidor_Hora.py
#  
#  
#  Purpose: Curso Python 2016 - UNRC
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import socket 
from datetime import datetime, date, time, timedelta

def main(): #definición de la fción principal.
    host="localhost" #Dirección IP del servidor
    port=8080
    nro_conex=5
    print """
    ******************************************
    SERVIDOR HORA (v1.0.0)
    CURSO: Introducción al lenguaje de programación python.
    - Ejemplo socket TCP -
    Licencia GNU GPL v2
    ******************************************
    """
    try:
        print "Listo..."
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creación del objeto socket.
        s.bind((host,port)) #Conecta el socket con la dirección especificada en el primer parámetro, a través del puerto del segundo parámetro
        s.listen(nro_conex) #"Escucha" conexiones, como máximo 5.
        c,client_address=s.accept() #Acepta al cliente "c"
        c.send("SERVIDOR-HORA-ACTUAL \n Status: ***Listo*** \n Indique la información que desea obtener:\n 1: Hora y minutos \n 2: Hora, minutos y segundos\n 3: Hora, minutos, segundos y microsegundos\n ** para salir\n")
        while(1):
            msg=c.recv(1024) #Recibe mensaje del cliente
            if msg=="**": #Cierra la conexión si el cliente envía el mensaje "**"
                print "Conexión cerrada desde remoto"
                break
            print(msg)
            while(msg<>'1' and msg<>'2' and msg<>'3'):
                c.send("Opción incorrecta, intente nuevamente.\n")
            hora = datetime.now();
            if msg=='1':
                info=str(hora.hour) + ":" + str(hora.minute);
                c.send("La hora actual es: "+ info);
                break;
            if msg=='2':
                info=str(hora.hour) + ":" + str(hora.minute)+ ":" + str(hora.second);
                c.send("La hora actual es: "+ info);
                break;
            if msg=='3':
                info=str(hora.hour) + ":" + str(hora.minute)+ ":" + str(hora.second)+ ":" + str(hora.microsecond);
                c.send("La hora actual es: "+ info);
                break;					
    except:
        try: 
            c.close()
            s.close()
        except:
            pass   
    finally:
        print "Finalizando. Gracias."
    return 0

if __name__ == '__main__':
	main()
	
