# -*- coding: utf-8 -*-
"""
    Globus Challenge

"""

from flask import Flask, g
app = Flask(__name__)


app.config.from_object('settings')


@app.route('/')
def challenge():
    return 'Globus Challenge'

