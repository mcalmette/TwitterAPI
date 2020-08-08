#pip install tweepy
"""
For Mac OS users: pip install pync

Credentials hold API key, secret key
access token and secret access token 
for each user -- not uploaded
"""
from Authenticator import TwitterAuthenticator, TwitterListener
from tweepy import Stream
from keywords import keyword_list
import pandas as pd



#Get streaming feature from API
class TwitterStreamer():
    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator
    def stream_tweets(self,fetched_tweets_filename,hash_tag_list):
        listener = TwitterListener(fetched_tweets_filename) #object listener
        auth = self.twitter_authenticator.authenticate_twitter_app(self)
        stream = Stream(auth, listener)
        stream.filter(track=hash_tag_list)


class TweetAnalyzer():
    #Analyzing content from tweets
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
        return df


if __name__ == "__main__":
    hash_tag_list = ["FDA Approval"]
    fetched_tweets_filename = "tweets.txt"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, keyword_list)