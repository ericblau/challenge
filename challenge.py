# -*- coding: utf-8 -*-
"""
    Globus Challenge

"""

from sqlite3 import dbapi2 as sqlite3
from flask import Flask, g
app = Flask(__name__)


app.config.from_object('settings')


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, app.config['DATABASE']):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database"""
    init_db()
    print 'Initialized the database'


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, app.config['DATABASE']):
        g.sqlite_db.close()


@app.route('/')
def challenge():
    return 'Globus Challenge'

