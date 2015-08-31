import random

# debug == true enables strange print statements for data validation
debug = True

# Sample Hangman class for practicing programming and python
# TODO: Add board drawing class
#		Add more words
# Author: Zack
class Hangman(object):
	"""This is not a real Hangman class"""
	
	# This is the initialization method for a Hangman game
	def __init__(self):
		self.health = 0

"""
	The method which carries out the turn-based play of Hangman game
"""
def play():

	wordlist = []

	# Open the list of words to read from
	fd = open('hangmanDictionary.txt', 'r')
	for line in fd:
		# Save the words to a list
		wordlist.append(line)

	# Get a random word to guess
	word = wordlist[random.randint(0, (len(wordlist) - 1))]

	###############
	if debug:
		print word
	###############

	# Have we won the game? 
	won = False

	# We've only won if we've guessed all the letters
	all_guesses = False

	# Keep track of all the letters that have been guessed
	guess = []

	while (not won):
		guess.append(raw_input('Please guess a letter: '))
		for letter in word:

			##############################################################
			if debug:
				print('Checking... is {} == {}'.format(guess[-1], letter))
			##############################################################

			if guess[-1] == letter:
				# Update board with a correct guess
				if all_guesses:
					won = True

				###################
				if debug:
					print "Correct!"
				###################

			else:
				# Update board with an incorrect guess

				
				######################
				if debug:
					print "Incorrect!"
				######################

play()