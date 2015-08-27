#! /usr/bin/python

import requests
import json

# Google Suggest URL found on Stack overflow: http://stackoverflow.com/questions/5102878/google-suggest-api
SUGGEST_URL= "http://google.com/complete/search?client=firefox&q="

def googleSuggest(query):
        #@query: phrase to search for suggestions
        #(ie what you'd type into Google.com)
        #returns a list of strings from the Google API
        #TODO: Exception handling
        r = requests.get(SUGGEST_URL + requests.utils.quote(query, safe=''))
        return r.json()[1] #JSON object [1] should be an array of results

def ppGS(query):
        #prints each result on a line
        for result in googleSuggest(query):
                print(result)
