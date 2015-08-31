import random

# Sample Hangman class for practicing with GitHub
# Author: Zack
class Hangman(object):
	"""This is not a real Hangman class"""
	
	# This is the initialization method for a Hangman game
	def __init__(self):
		self.health = 0

wordlist = []

# Open the list of words to read from
fd = open('hangmanDictionary.txt', 'r')
for line in fd:
	# Save the words to a list
	wordlist.append(line)

# Get a random word to guess
word = wordlist[random.randint(0, len(wordlist))]

