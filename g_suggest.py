#! /usr/bin/python3

import requests
import logging

# Google Suggest URL found on Stack overflow: http://stackoverflow.com/questions/5102878/google-suggest-api
SUGGEST_URL= "http://google.com/complete/search?client=firefox&q="

def googleSuggest(query):
        # @query: phrase to search for suggestions
        # (ie what you'd type into Google.com)
        # returns a list of strings from the Google API
        try:
            r = requests.get(SUGGEST_URL + requests.utils.quote(query, safe=''))
            r.raise_for_status()
            return r.json()[1] #JSON object [1] should be an array of results
        except (ValueError, requests.exceptions.HTTPError) as e:
            logging.error("Bad request or invalid response. %s", e)
            return None

def ppGS(query):
        #prints each result on a line, for trying it out in console
        for result in googleSuggest(query):
                print(result)