#!/usr/bin/python3
"""
Script that starts a Flask web application with five routes
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display C followed by text value"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Display Python followed by text value"""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display "n is a number" only if n is an integer"""
    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)