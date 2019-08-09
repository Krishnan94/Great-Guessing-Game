'''
This file contains the gameplay function required to play the game
Global variable declarationis present in DATA
 Frequency : Dictonary which has all the letters with the frequency
 foundchar : list of found charcters
 missedguess : list of count of missed letter in a game
 badguess : list of count of bad guess in a game
 wordused :  list of words used in a game
 status : list of status in a game
 score : lsit of scores of each game
 count : count of number of time letter function is called
 badguesscount : count of bad guess in a game
 missedcount : count of wrong letter guess ina a game
 totalscore : score of a game
 currentstatus : status of a game
'''
frequency = {'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.7, 'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97,'z': 0.07}
'''
 Dictonary which has all the letters with the frequency
'''
foundchar = ["-"]*4
missedguess = []
badguess = []
wordsused = []
status = []
score = []
count=0
badguesscount= 0
missedcount = 0
totalscore = 0
currentstatus = ""
class game:
	def guess(self,currentword,currentcharc):
		'''
		This function takes current word and character of current word as input and guess word from user and check if the guess word and current word are same
		if they are same then we calculate the total score and update each value in updatevalue function
		:param currentword: string -word in which the user is playing
		:param currentcharc: list- list of current word
		:return: true if guess is correct else false
		'''
		guessword=raw_input("Enter the word \n")
		guessword=guessword.lower()
		if guessword==currentword:
			print("Congrats! you  found the word")
			currentstatus= "Success"
			j = 0
			i = 0
			global totalscore
			for j in range(len(foundchar)):
				if foundchar[j] == '-':
					totalscore=totalscore+frequency[currentcharc[j]]
			if count == 0 :
				totalscore = totalscore
			else :
				totalscore=totalscore/count
			totalscore = round(totalscore, 2)
			self.valueUpdate(currentstatus, totalscore, currentword)
			return True
		else:
			print("Sorry! your guess is wrong")
			global badguesscount
			badguesscount = badguesscount+1			
			return False


	def prints(self):
		'''
		This function prints the current guess after every letter and incorrect guess call
		'''
		print("Current Guess:" + foundchar[0]+foundchar[1]+foundchar[2]+foundchar[3])


	def valueUpdate(self,stat, total, currentword):
		'''
		This function updates the value after every correct guess , tell me and quit after few guess is called
		It Updates score,word,status,badguess all in the corresponding list
		:param stat: status of the current game
		:param total: score of the game
		:param currentword: current word in which the user is playing the game
		'''
		global missedcount
		global badguesscount
		global foundchar
		global count
		wordsused.append(currentword)
		badguess.append(badguesscount)
		status.append(stat)
		missedguess.append(missedcount)
		total = round(total, 2)
		if stat == "Gave up":
			score.append(-total)
		else:
			total = total - ((badguesscount*0.1)*total)
			total = round(total, 2)
			score.append(total)
		totalscore=0
		foundchar = ['-']*4
		badguesscount=0
		missedcount=0
		count=0
		currentstatus = ""


	def quit(self,currentword,currentchar):
		'''
		This function is called when the q key is pressed in the game
		This function prints the values of all the game played till now by the user
		:param currentword: current word the user is playing
		:param currentchar: list of current word
		'''
		if count !=0 or badguesscount != 0 :
			self.tellme(currentchar,currentword)
		print("Game \t word \t status  \t BadGuess \t Missed Letters \t score ")
		print("---- \t ---- \t ------- \t -------- \t -------------- \t ----- ")
		head = "Game\tword\tstatus\tBadGuess\tMissed Letters\tScore\n"
		fmt = "{Game:d}\t{word:s}\t{status:s}\t{BadGuess:d}\t{Missed Letters:d}\t{Score:0.2f}\n"
		j = 1
		finalscore = 0
		for temp in score:
			finalscore = finalscore + temp
		for j in range(len(wordsused)):
			t=j+1
			#print fmt.format(Game=t, word=wordsused[j], status=status[j], BadGuess=badguess[j], {Missed Letter}=)
			print(str(t) + "        " + wordsused[j] + "    " + str(status[j]) + "         " + str(badguess[j]) + "               " + str(missedguess[j]) + "                       " + str(score[j]))
		finalscore= round(finalscore,2)
		print("\n Final Score :"+ str(finalscore))

	def letter(self,currentcharc):
		'''
		This function is called when the l key is pressed in the game
		This function checks if the letter entered by the used is present in the current word
		:param currentcharc: list of current word
		'''
		global count
		count = count + 1
		letters = raw_input("Enter a letter \n")
		letters=letters.lower()
		i = 0
		k = 0
		j = 0
		for j in range(len(currentcharc)):
			if currentcharc[j] == letters:
				foundchar[j] = letters
				# if foundchar=currentcharc
				k = k + 1			
		# prints()
		if k == 0:
			print("Sorry! Letter Not Found")
			global missedcount
			missedcount = missedcount + 1
		elif k > 0:
			print("You have found " + str(k) + " letter")		


	def tellme(self,currentcharc,currentword):
		'''
		This function is called  when t is pressed in the game
		This function changes the status to Gave Up and calculate the total score of the game by adding the un covered letter with a negative sign
		:param currentcharc: list of current word
		:param currentword: current word of the game
		'''
		print ("Lost! you just missed a easy word")
		print ("The word is " + currentword)
		currentstatus = "Gave up"
		global missedcount
		global totalscore
		j=0
		for j in range(len(foundchar)):
			if foundchar[j] == '-':
				totalscore = totalscore + frequency[currentcharc[j]]
		self.valueUpdate(currentstatus, totalscore,currentword)
