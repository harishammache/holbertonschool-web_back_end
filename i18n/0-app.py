#!/usr/bin/env python3
"""Basic Flask app with a single route."""


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Renders the home page with a welcome message."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run()