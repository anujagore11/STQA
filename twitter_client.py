import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():
    """Setup Twitter authentication.
    Return: tweepy.OAuthHandler object
    """
    try:
        consumer_key = "fJriwU9JcNHkzAJYJ7PoI7ftH"
        consumer_secret="0h7hGZitUT3l4p6WawTVoPdPE9NNyvfhGixi7EBVPh1pjwfQ7c"
        access_token ="1084095074-K4hbfrQZpEGbtacf8y1FZmflrHc7RkZtssdUnZt"
        access_secret ="hXy7OuQhg855PQqsHo0TpeotFvntzkpNs89BB6KpmgsV8"
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

def get_twitter_client():
    """Setup Twitter API client.
    Return: tweepy.API object
    """
    auth = get_twitter_auth()
    client = API(auth)
    return client
			
			
