#!/usr/bin/env python3
"""jk les lkjnkjsv kjkjjbkjl sdjb jlsdlk lkjds"""
from flask import Flask
from flask import request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """s sdvbj jhhbsdv jbhjhbksdvjh bkbdsv"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# xf
app = Flask(__name__)
app.config.from_object(Config)

# xf
babel = Babel(app)


@babel.localeselector
def get_locale():
    """,nx jlkjk;xf kjnklj klkn kjnlxkf lknkljxf"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """jk bhbjbvsdbj bhb ljbsdlbv njksd"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
