#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import socket
import sys
from time import sleep
from progress.bar import Bar
from clint.textui import progress
from progress.spinner import PixelSpinner

def test1():        
    print('Processing client request...')
    for i in progress.mill(range(100)):
        sleep(0.02)
        
def test2():
    with PixelSpinner('Communicating with server...') as bar:
        for i in range(100):
            sleep(0.06)
            bar.next()
    print('Processing server data...')
    for i in progress.mill(range(100)):
        sleep(0.02)
       
    print('Resolving dependencies...')
    for i in progress.mill(range(100)):
        sleep(0.02)
    print("action is complete.")
        
def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = 8888

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    print("Enter 'quit' to exit")
    message = input(" -> ")

    while message != 'quit':
        soc.sendall(message.encode("utf8"))
        rec = soc.recv(5120).decode("utf8")
        if rec == "-":
            pass     
        elif rec == "command to client":
            print("Client recieved: (" + rec +") test complete")
            test1()
            test2()
            pass 
              

        message = input(" -> ")

    soc.send(b'--quit--')

if __name__ == "__main__":
    main()