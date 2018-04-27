import json
data = json.load(open("data.json"))
def translate(w):
    w.lower()
    if w in data:
        return data[w]
    else:
        return "The word does not exist. Please double check it."
#this is where the prongram starts
word = input ("Enter word: ")
print(translate(word))
