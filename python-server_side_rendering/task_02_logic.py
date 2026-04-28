#!/usr/bin/python3
"""Flask app with dynamic template logic."""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def home():
    """Render home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render items page with JSON data."""
    with open('items.json', 'r') as file:
        data = json.load(file)

    items_list = data.get("items", [])
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
