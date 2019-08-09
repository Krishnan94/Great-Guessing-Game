'''
This file contains the main menu for the play
Glabal variable decarled in the Data 
  Outerloop : Boolean value for the new game
  innerloop : Boolean value for the continue game
'''
from stringDataBase import stringDataBase
from game import game

outerloop=True
innerloop=True

class Guess:
	       	
	def game(self):
		currentgame=game()
		data = stringDataBase()
		for i in range(1,101):
			global outerloop 
			global innerloop
			if outerloop==False and innerloop==False:
				break
			data.getallword()			
			while(outerloop):
				currentword = data.getword()
				print(currentword)
				currentchar = list(currentword)
				print("** The great guessing game **")
				print("Current Guess: ----")
				innerloop = True
				while innerloop:
					choose = raw_input("g=guess,t=tell me,l for a letter,and q to quit \n")
					choose=choose.lower()
					if choose == 'g':
						guessword = currentgame.guess(currentword,currentchar)
						if guessword:
							innerloop=False
						else:
							currentgame.prints()
					elif choose == 'l':
						currentgame.letter(currentchar)
						currentgame.prints()
					elif choose == 't':
						currentgame.tellme(currentchar,currentword)
						innerloop=False
					elif choose == 'q':
						currentgame.quit(currentword,currentchar)
						innerloop=False
						outerloop=False
						

guess=Guess()
guess.game()
