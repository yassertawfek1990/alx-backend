#!/usr/bin/env python3
""",jnsd kjnksnkj lksdkj klj kljsknlkjsc"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """bhjbsdl blkjsdv kn kjsndl vn"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
