#!/usr/bin/python3
"""
Script that starts a Flask web application with states list
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display HTML page with list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=sorted(states, key=lambda x: x.name))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)