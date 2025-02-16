#!/usr/bin/python3
"""
Script that starts a Flask web application with states and cities
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()

@app.route('/states', strict_slashes=False)
def states_list():
    """Display HTML page with list of states"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=sorted(states, key=lambda x: x.name))

@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Display HTML page with state info by id"""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', not_found=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)