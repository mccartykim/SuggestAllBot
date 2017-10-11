#! /usr/bin/python


import json
import tweepy
import os
from db import load_tweet

# TODO revise whole thing to work with cloud storage
#I've stored my own keys in a json file.  Hopefully, between my names and the tweepy
#docs, this makes sense.
def main():
    auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
    auth.set_access_token(os.environ["TWITTER_KEY"], os.environ["TWITTER_SECRET"])
    twit_api = tweepy.API(auth)
    try:
        tweet = load_tweet()
    except IndexError:
        import tweet_maker
        tweet_maker.main()
        tweet = load_tweet()
    twit_api.update_status(tweet)


if __name__ == "__main__":
    main()
