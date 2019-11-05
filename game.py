# import rndm package for rndm choices
from random import randint
# import time module
import time
from gameFunctions import score

# Choices array
choices = ["Rock", "Paper", "Scissors"]

# Set the computer's choice
computer = choices[randint(0,2)]

# set up game loop and other variables
player = False
pScore = 0
cScore = 0
cWin = False

#functions


while player == False:
	# set player to True
	print("******************************** \n")
	time.sleep(1)
	print("Type quit at any time to exit\n")
	print("******************************** \n")

	player = input("choose rock, paper or scissors\n")
	player = player.lower()
	player = player.capitalize()

	# Check quit
	if player == "Quit":
		exit()
	else:
		# results timer
		timerMessage = ["********************************\n", "******** ROCK *********\n", "******** PAPER ********\n", "******* SCISSORS ******\n"]
		x=0
		while x<4:
			print(timerMessage[x])
			time.sleep(.5)
			x=x+1

		# Ruslts
		print("******************************** \n")
		print("Computer chose ", computer, "\n" )
		print("Player chose ", player, "\n" )

	time.sleep(1)
	if computer == player:
		print("It's a Tie")
		score.showScore(cWin, cScore, pScore)
	
	elif player == "Rock":
		if computer == "Paper":
			print("You lose!", computer, "Covers", player, "\n")
			cScore = cScore + 1
			cWin = True
		else:
			print("You win!", player, "Smashes", computer, "\n")
			pScore = pScore + 1
			cWin = False
		score.showScore(cWin, cScore, pScore)
	
	elif player == "Paper":
		if computer == "Scissors":
			print("You lose!", computer, "Cuts", player, "\n")
			cScore = cScore + 1
			cWin = True
		else:
			print("You win!", player, "Covers", computer, "\n")
			pScore = pScore + 1
			cWin = False
		score.showScore()
	
	elif player == "Scissors":
		if computer == "Rock":
			print("You lose!", computer, "Smashes", player, "\n")
			cScore = cScore + 1
			cWin = True
		else:
			print("You win!", player, "Cuts", computer, "\n")
			pScore = pScore + 1
			cWin = False
		score.showScore()
	else:
		print("That's not a valid choice")
		

	

	player = False
	computer = choices[randint(0,2)]


