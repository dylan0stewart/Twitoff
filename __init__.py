"""Entry point for Twitoff Flask Application"""

from .app import create_app
from flask_sqlalchemy import SQLAlchemy

APP = create_app()