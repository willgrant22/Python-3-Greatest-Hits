#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Author :  Will Grant
# =============================================================================

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():

    return 'Home page'


@app.route('/greet', methods=['GET'])
def greet():

    name = request.args.get('name', 'Guest')
    msg = f'Hello {name}\n'

    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}

#curl -i localhost:5000/greet?name=Will
#localhost:5000/greet?name=Will
