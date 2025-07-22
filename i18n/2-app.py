#!/usr/bin/env python3
"""Basic Flask app with a single route."""


from flask_babel import Babel
from flask import Flask, render_template, request


babel = Babel()


class Config():
    """that has a LANGUAGES class attribute"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """get_locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def index() -> str:
    """Renders the home page with a welcome message."""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
