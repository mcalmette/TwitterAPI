#pip install tweepy
"""
For Mac OS users: pip install pync
"""
import json
from pync import Notifier
from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#import numpy as np
import pandas as pd
"""
Credentials hold API key, secret key
access token and secret access token 
for each user -- not uploaded
"""
import credentials


"""
Get streaming feature from API
"""

#auth class
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(credentials.api_key, credentials.api_key_secret)
        auth.set_access_token(credentials.access_token, credentials.access_token_secret)
        return auth

class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator
    def stream_tweets(self,fetched_tweets_filename,hash_tag_list):
        listener = TwitterListener(fetched_tweets_filename) #object listener
        auth = self.twitter_authenticator.authenticate_twitter_app(self)
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)

class TwitterListener(StreamListener):

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, raw_data):
        try:
            y = json.loads(raw_data)
            print("Text:", y['text'])
            print("In Reply to:", y['in_reply_to_screen_name'])
            Notifier.notify(y['text'], title='Python')
            #with open() as tf:
                #tf.write(raw_data)
            return True
        except BaseException as e:
            print("Error on data %s" % str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            return False
        print(status_code)


class TweetAnalyzer():
    """
    Analyzing content from tweets
    """
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        return df

if __name__ == "__main__":
    hash_tag_list = ["VXRT","Inpixon","inpixon"]
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
