'''
Main applicaion and routing logic for Twitoff
'''
from flask import Flask
from .models import DB

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)
    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'

    return app
