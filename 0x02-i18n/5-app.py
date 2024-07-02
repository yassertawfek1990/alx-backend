#!/usr/bin/env python3
"""jhjbjhasb cb lkjabsjkc bkjabsclkj"""
from typing import (
    Dict, Union
)

from flask import Flask
from flask import g, request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """jhvhjsd kjkjl skjd jbkljasbc llkj as; mh,asx"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """jgkj sbd nkjnsdn clknskldc,jhbj dsc kjds"""
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """khkjhsd lckjh lkjsd cjb"""
    return users.get(int(id), 0)


@app.before_request
def before_request():
    """,kjskjd ckjn;ksdn n;sdcsdvds"""
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    """ksbldbck bdslkcb kjsdb chhj hjbkdshhjck hjsdchj"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
