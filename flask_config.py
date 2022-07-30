"""
Instance config file
"""


import os

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABADE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'aubay_appdb.db')

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = ''

FLASK_HOST = 'localhost'

FLASK_PORT = 7200