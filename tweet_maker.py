#! /usr/bin/python

from g_suggest import googleSuggest
import json
import db

# TODO sadly I think this might call for an entire rewrite for the SQL support

def main():
    """
    This function will read the next query in query.txt, using the info saved in
    state.json to remember settings
    It will then find the google suggestions, and save them for later tweets
    And finally, it will save its state for the next time the script is called.
    """
    query = db.get_query()
    length = len(query.text.split())
    # If a suggestion is longer than this length, store query strings that are one longer for future suggestions
    suggestions = googleSuggest(query.text)
    appendQueries(suggestions, length+1)
    db.store_responses(suggestions, query.text)


def appendQueries(suggestionList, length):
    #Collect a list of suggestions from each of the first n suggestions, eliminating repetitions
    query_list = []
    for suggestion in suggestionList:
        try:
            query = suggestion.split()[0:length+1]
            if query not in query_list:
                query_list.append(" ".join(query))
        except IndexError:
            pass #if it was shorter than n, for whatever reason, it was probably already in the list...
    db.store_queries(query_list)


if __name__ == "__main__":
    main()
