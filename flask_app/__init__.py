# -*- coding: utf-8 -*-

"""Top-level package for flask_app."""

__author__ = """Aoife O Sullivan"""
__email__ = 'aoifeosullivan19@gmail.com'
__version__ = '0.1'

from flask import Flask
app = Flask(__name__)
from flask_app import views
