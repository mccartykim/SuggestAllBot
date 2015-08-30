#! /usr/bin/python

import json
import tweepy

#I've stored my own keys in a json file.  Hopefully, between my names and the tweepy
#docs, this makes sense.
def main():
    with open("state.json", "r") as state_json:
        tweet_index = json.load(state_json)["tweet_index"]
    with open("keys.json", 'r') as keys_json:
        keys = json.load(keys_json)
    auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
    auth.set_access_token(keys["access_token"], keys["access_token_secret"])
    twit_api = tweepy.API(auth)
    twit_api.update_status(status=load_tweet(tweet_index))
    state = {}
    with open("state.json", "r") as state_json:
        state = json.load(state_json)
    state["tweet_index"] = tweet_index + 1
    with open("state.json", "w") as state_json:
        state["tweet_index"] = tweet_index + 1
        json.dump(state, state_json)

def load_tweet(line):
    with open("full_list.txt", "r") as full_list:
        for line_num, tweet in enumerate(full_list):
            if line == line_num:
                return tweet
        #if the loop exits, line was not in the file.  We invoke tweet_maker
    import tweet_maker
    tweet_maker.main()
    return load_tweet(line) #recall this function, as the list should be full.
        

if __name__ == "__main__":
    main()
