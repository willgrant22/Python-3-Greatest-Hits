#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from ssh import ssh
sshUsername = ""
sshPassword = ""
sshServer = ""

connection = ssh(sshServer, sshUsername, sshPassword)
connection.openShell()
while True:
    command = input('$ ')
    if command.startswith(" "):
        command = command[1:]
    connection.sendShell(command)