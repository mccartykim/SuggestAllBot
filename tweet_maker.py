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
    appendQueries(suggestions, n)
    appendTweets(suggestions)
    saveState(i, n)
    
def loadState():
    with open("state.json", "r") as state_file:
        result = json.load(state_file)
    return result #would it be bad form to return this above?  who knows...

def loadWord(index):
    with open("queries.txt", "r") as words:
        for i, word in enumerate(words):
            if i == index:
                return word
            elif(i > index):
                return "error"

def saveState(index, length):
    with open("state.json", "w") as state_file:
        output = {"index": index, "length": length}
        json.dump(output)

def appendQueries(suggestionList, length):
    #Collect a list of suggestions from each of the first n suggestions, eliminating repetitions
    query_list = []
    for suggestion in suggestionList:
        try:
            query = suggestion.split()[0:length+1]
            if query not in query_list:
                query_list.append(word)
        except IndexError:
            pass #if it was shorter than n, for whatever reason, it was probably already in the list...
    with open("queries.txt", "a") as state_file:
        for query in query_list:
            state_file.write(word + "\n")

def appendTweets(suggestionList):
    with open("first_list.txt", "a") as first_list:
        first_list.write(suggestionList[0] + "\n")
    with open("full_list.txt", "a") as full_list:
        for suggestion in suggestionList:
            full_list.write(suggestion + "\n")
    
if __name__ == "__main__":
    main()
