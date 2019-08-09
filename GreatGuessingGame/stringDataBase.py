'''
This file contains the function to read all the word from the file and get a word from the list using random function
Global Variable declaration present in DATA
 wordList : contains list of word read from the file
'''
import random

wordList = []

class stringDataBase:
	def getallword(self):
	    '''This function takes all the words from the file and store it in the list'''
	    file = open("four_letters.txt", "r")
	    for line in file:
		newline = line.split()
		for temp in newline:
		        wordList.append(temp)




	def getword(self):
	    ''' This function returns a random word from the list
		:return: random word from the list
	     '''
	    k = random.randrange(0, 4030)
	    currentword = wordList[k]
	    return currentword
