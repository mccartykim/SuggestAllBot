#! /usr/bin/python

from g_suggest import googleSuggest
import json

def main():
    """
    This function will read the next query in query.txt, using the info saved in
    state.json to remember settings
    It will then find the google suggestions, and save them for later tweets
    And finally, it will save its state for the next time the script is called.
    """
    state = loadState()
    i = state["index"]
    word_count = state["length"]
    word = loadWord(i)
    # If a suggestion is longer than this length, store query strings that are one longer for future suggestions
    if (len(word.split()) > word_count):
        word_count += 1
    suggestions = googleSuggest(word)
    appendQueries(suggestions, word_count)
    appendTweets(suggestions)
    saveState(i+1, word_count)

    
def loadState():
    result = None
    with open("state.json", "r") as state_file:
        result = json.load(state_file)
    return result 


def loadWord(index):
    with open("queries.txt", "r") as words:
        for i, word in enumerate(words):
            if i == index:
                return word
            elif(i > index):
                return "error"


def saveState(index, length):
    state = {}
    with open("state.json", "r") as state_file:
        state = json.load(state_file)
    with open("state.json", "w") as state_file:
        state["index"] = index
        state["length"] = length
        json.dump(state, state_file)


def appendQueries(suggestionList, length):
    #Collect a list of suggestions from each of the first n suggestions, eliminating repetitions
    query_list = []
    for suggestion in suggestionList:
        try:
            query = suggestion.split()[0:length+1]
            if query not in query_list:
                query_list.append(query)
        except IndexError:
            pass #if it was shorter than n, for whatever reason, it was probably already in the list...
    with open("queries.txt", "a") as state_file:
        for query in query_list:
            print(query)
            state_file.write(" ".join(query) + "\n")


def appendTweets(suggestionList):
    with open("first_list.txt", "a") as first_list:
        first_list.write(suggestionList[0] + "\n")
    with open("full_list.txt", "a") as full_list:
        for suggestion in suggestionList:
            full_list.write(suggestion + "\n")
    

if __name__ == "__main__":
    main()
