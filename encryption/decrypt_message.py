#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from cryptography.fernet import Fernet

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())

if __name__ == "__main__":
    decrypt_message(b'gAAAAABe992qCr0R5OxNCFNRad-XOrUTB6vexsH7PlqApXFB_DSlgPknwPRCSnWSMWtu1NhAS6zq9acfkDjzdT3jzpvWp9BJuUmfebFCYdQibMW7Bl2rUFg=')