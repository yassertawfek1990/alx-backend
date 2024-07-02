#!/usr/bin/env python3
"""khklh kjew klj nkj nwjq;cn lkqw"""
from flask import Flask
from flask import request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """kugwlueu ckjkj;q;kdn kjnkjwnqkcjb"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# I
app = Flask(__name__)
app.config.from_object(Config)

# W
babel = Babel(app)


@babel.localeselector
def get_locale():
    """sdckjkn ;ksnc ;nk;nalsk cn;knlskdc"""
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """klkj sdjn kjsndj cnkjn ksdc"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
