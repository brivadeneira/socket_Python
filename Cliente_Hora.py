#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Cliente_Hora.py
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

def main():
    host="localhost"
    port=8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    while(1):
        msg_recv=s.recv(1024)
        print msg_recv
        msg=raw_input("Msg2Send>> ")
        s.send(msg)
        if msg=="**":
            print "Conexión cerrada"
            break
    s.close()
    return 0

if __name__ == '__main__':
	main()

