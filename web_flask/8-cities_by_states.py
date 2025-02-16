#!/usr/bin/python3
"""
Script that starts a Flask web application with cities by states
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display HTML page with list of cities by states"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=sorted(states, key=lambda x: x.name))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)