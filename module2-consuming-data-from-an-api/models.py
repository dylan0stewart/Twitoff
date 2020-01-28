'''SQLAlchemy models for Twitoff'''
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()



class User(DB.Model):
    '''Twitter users we pull and analyze tweets for.'''
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

class Tweet(DB.Model):
    '''Tweets'''
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))