#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():

    return 'Home page'


@app.route("/greet/<name>/")
def greet(name):

    msg = f'Hello {name}\n'

    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}

#curl localhost:5000/greet/Will/
