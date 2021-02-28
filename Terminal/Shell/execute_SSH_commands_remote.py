#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

import paramiko

hostname = "192.168.1.1"
username = ""
password = ""

commands = [
    "pwd",
    "id",
    "uname -a",
    "df -h"
]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

for command in commands:
    print("="*50, command, "="*50)
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    err = stderr.read().decode()
    if err:
        print(err)    

client.close()