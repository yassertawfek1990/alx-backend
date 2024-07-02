#!/usr/bin/env python3
"""askjxhxklj kjakjs ckjlkjj lkjn ask;jcn k;jnasc nkjlascx"""
from flask_babel import Babel
from typing import Union, Dict
from flask import Flask, render_template, request, g


class Config:
    """kak jkjb kbsdlcbkj kjlk.sdn ckjbkjbkjandcn;k;"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """kbkj bbkjlals ckjb klb kjablcb lblka blck blask"""
    login_id = request.args.get('login_as', '')
    if login_id:
        return users.get(int(login_id), None)
    return None


@app.before_request
def before_request() -> None:
    """jhsdkjhb cb jb sbd kcbkjlkj kjsbdcbkjb kh bdskcdscjbj"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """klkw  blkjblkj slkjcb jbl kh ksh dckjb,k b,djbcjhbkjblbkjjkjas"""
    locale = request.args.get('locale', '')
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """mjbk,jsb dck nk n ;kajsc .kn jsajxhbkjasnx jabhjbc jhas"""
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
