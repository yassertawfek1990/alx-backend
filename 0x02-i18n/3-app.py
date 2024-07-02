#!/usr/bin/env python3
"""sdklj kjsdkj klb lkjsdkl lk lkdsdlk ks"""
from flask import Flask
from flask import request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """kuahluh  kjbhkh bash bbshaa"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """kbkljb sjldb clb lkjbsdc kjkjl dsl"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """kblskb c.kna cnlkn jasc lkh;;nans;lc;;"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
