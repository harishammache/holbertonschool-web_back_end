#!/usr/bin/env python3
"""Basic Flask app with a single route."""


from flask_babel import Babel
from flask import Flask, render_template

app = Flask(__name__)


babel = Babel()


class Config():
    """that has a LANGUAGES class attribute"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel.init_app(app)


@app.route('/')
def index() -> str:
    """Renders the home page with a welcome message."""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
