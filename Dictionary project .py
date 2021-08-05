import json
from difflib import get_close_matches

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no:- ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("Sorry sir no word exist")
        else:
            return("Please enter y and n")

    else:
        return("There is no such word exist")


data = json.load(open("data.json"))
word = input("Enter the word you want to search:- ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)