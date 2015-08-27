from g_suggest import googleSuggest
import json

def main():
    """
    Rough plan: This script will be called by cron or a similar scheduler.
    Every time it's called, it will check the index from a saved file, and hash a word from that index in the words.txt file
    It will append the words.txt file with the first unique two (or n+1 on later iterations) words of each result.
    (This will probably require helper functions)
    Finally, it appends a buffer of tweets, and saves its index.    
    """
    state = loadState()
    i = state["index"]
    n = state["length"]
    
    word = loadWord(i)
    suggestions = googleSuggest(word)
    appendWords(suggestions)
    appendTweets(suggestions)
    saveIndex(i)
    
def loadState():
    with open("state.json", "r") as state_file:
        result = json.load(state_file)
    return result #would it be bad form to return this above?  who knows...

def loadWord(index):
    with open("words.txt", "r") as words:
        for i, word in enumerate(words):
            if i == index:
                return word
            elif(i > index):
                return "error"

def appendWords(suggestionList):
    
    
if __name__ == "__main__":
    main()
