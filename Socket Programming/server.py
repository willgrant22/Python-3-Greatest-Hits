#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import socket

s = socket.socket()

ip_address = socket.gethostbyname(socket.gethostname())

s.bind((ip_address, 12345))

s.listen(3)

print("Server ip address:", ip_address)

while True:
    print('waiting for a connection')
    connection, client_address = s.accept()
    try:

        print('connected from', client_address)

        connection.send(str("Now You are connected").encode("utf-8"))

        while True:
            data = connection.recv(1024).decode("utf-8")
            if data:

                print(list(client_address)[0], end="")
                print(": %s" % data)

                new_data = str(input("You: ")).encode("utf-8")
                connection.send(new_data)
    finally:

        connection.close()
