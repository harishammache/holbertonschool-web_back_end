#!/usr/bin/env python3
"""Basic Flask app with a single route."""


from flask_babel import Babel, _
from flask import Flask, render_template, request, g
import pytz
from pytz.exceptions import UnknownTimeZoneError


babel = Babel()


class Config():
    """that has a LANGUAGES class attribute"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """mathode get"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.get('user'):
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """Renders the home page with a welcome message."""
    return render_template('7-index.html', get_locale=get_locale,  _=_)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """methode get_user"""
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """methode before"""
    g.user = get_user()


def get_timezone():
    """methode get"""
    tz = request.args.get('timezone')
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass

    if g.get('user'):
        user_tz = g.user.get('timezone')
        if user_tz:
            try:
                pytz.timezone(user_tz)
                return user_tz
            except UnknownTimeZoneError:
                pass

    return 'UTC'

babel.init_app(app, timezone_selector=get_timezone)


if __name__ == '__main__':
    app.run()
