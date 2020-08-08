#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello there!'

