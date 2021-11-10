#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Will Grant
# Description : Encrypt file with Aes
# =============================================================================

import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "4VJ8q9,(3D?'gTUl/(>8.$O4&$uVT'0M"
# encrypt
pyAesCrypt.encryptFile("data.db", "data.AstLock", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("data.AstLock", "dataout.db", password, bufferSize)