#pip install tweepy

import tweepy
from textblob import TextBlob

consumer_key = "api_key"
consumer_secret = "api_key_secret"

access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets("Trump")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

## It does not work becasuse of twitter api v2

