import json

from difflib import get_close_matches

data = json.load(open("data1.1.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]

	elif word.title() in data:
		return data[word.title()]

	elif word.upper() in data:
		return data[word.upper()]

	elif len(get_close_matches(word,data.keys(),1,0.6))>0:
		y_or_n = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
		if y_or_n[0].lower() == 'y':
			return data[get_close_matches(word, data.keys())[0]]
		elif y_or_n[0].lower() == 'n':
			return "The word doesn't exist. Please double check it."

		else:
			return "The word doesn't exist. Please double check it."
	else:
		return "The word doesn't exist. Please double check it"
word = input("Enter word: ")
output = translate(word)

if type(output) == list:
	for item in output:
		print (item)

else:
	print(output)