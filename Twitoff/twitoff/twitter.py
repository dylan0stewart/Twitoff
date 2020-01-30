
import basilica
import tweepy
from decouple import config

from twitoff.models import User


TWITTER_AUTH = tweepy.OAuthHandler(config('TgnWFuhpqdGL1RRcZbFtRWhN43'), config('ETNfYA1JDqZPyDIgfUhee4S8jM14btVyD5Adw1cgnfivC4igwA'))
TWITTER_AUTH.set_access_token(config('1221834263273857026-mYpdAYf5XGmHxmSwCP5n17E40z97lr'), config('pTIB00bxKXitaPvXB7fZZdyTd9faQidOnWGGB5hvU9ujj'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(config("37f31a6a-e50f-c962-be30-a75fba86bca5"))

def add_or_update_user(name):
    """ 
    Add or update a user and their Tweets.
    Throw an error if user doesn't exist or is private
    """
    try:
        twitter_user = TWITTER.get_user(name)
        db_user = User.query.get(twitter_user.id)

    except:

    else: