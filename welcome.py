import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        err = input ("Did you mean %s instead (y/n)? " % get_close_matches(w,data.keys()) [0])
        #return "Did you mean %s instead? " % get_close_matches(w,data.keys()) [0]
        if err == "y":
            return data[get_close_matches(w,data.keys()) [0]]
        else:
            return "The word does not exist. Please double check it."

    else:
        return "The word does not exist. Please double check it."
#this is where the prongram starts
word = input ("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
        print(output)
