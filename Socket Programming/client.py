#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import socket

s = socket.socket()

server = input("Enter Server IP: ")

s.connect((server, 12345))

data = s.recv(1024).decode("utf-8")
print(server + ": " + data)

while True:

    new_data = str(input("You: ")).encode("utf-8")
    s.sendall(new_data)

    data = s.recv(1024).decode("utf-8")
    print(server + ": " + data)

s.close()
