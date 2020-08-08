from tweepy import OAuthHandler
from tweepy import StreamListener
from pync import Notifier
import json
import credentials

class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(credentials.api_key, credentials.api_key_secret)
        auth.set_access_token(credentials.access_token, credentials.access_token_secret)
        return auth

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