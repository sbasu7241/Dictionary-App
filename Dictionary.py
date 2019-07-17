"""A dictionary app"""

import nltk # Natural Language Text Processing
import pyperclip # To get clipboard data and feed it into the dictionary
import ctypes # To pop up message box
import time
import re # Regular Expression might be needed
import sys 
from nltk.corpus import wordnet # Dictionary database access 

def stop():
	sys.exit() # To exit the app

def run(timer=2):

	default = "NoVal"
	
	print('\n***** WELCOME TO THE PYTHON ENGLISH DICTIONARY *****\n')

	#nltk.download("wordnet") # We will be using wordnet to get meanings,antonyms and synonyms

	time_in_sec = timer * 3600

	start_time = time.time()

	ti = time.gmtime() 

	print ("Time of starting program : ",end="") 
	print (time.asctime(ti))

	while True and time.time() - start_time < time_in_sec:

		word=pyperclip.paste() # Extract word from clipboard

		word=re.sub('[^A-Za-z]+','', word) # Remove all non alphabet characters using re

		word = word.lower()

		time.sleep(1) # Pause for user to copy text

		if word != default: # If word is not the old one
			
			print("\n* Extracted from clipboard : {}".format(word))

			print("Seaching for word: {} in dictionary".format(word))

			
			define=wordnet.synsets(word) # Find synsets of word

			definition = "Searching for word : " + word +"\n\n" + "Meaning : \n"

			# Word meanings

			ctr = 1 # Loop counter
			
			for j in define:
				
				message = str(ctr) + '. ' + j.definition() + '\n'
				definition += "\n" + message 
				ctr += 1


			# Synonyms and antonyms

			synonyms = []
			antonyms = []

			for j in define:

				for i in j.lemmas():

					synonyms.append(i.name()) # get synonyms
					if i.antonyms():
						antonyms.append(i.antonyms()[0].name()) # get antonyms

			synonyms = set(synonyms)
			antonyms = set(antonyms)

			# Window pop up box displaying the word its meaning and antonyms and synonyms

			# For windows users 

			ctypes.windll.user32.MessageBoxW(0, definition+'\n\nSynonyms: '+', '.join(synonyms)+'\n\nAntonyms: '+', '.join(antonyms), 'Word Meaning - '+word, 0)

			# Linux users comment out the above line and uncomment the line below

			# alert(text=definitions+'\n\nSynonyms: '+', '.join(synonyms)+'\n\nAntonyms: '+', '.join(antonyms), title='Word Meaning - '+word, button='OK')

			default = word


if __name__ == "__main__":
	run()
























run()