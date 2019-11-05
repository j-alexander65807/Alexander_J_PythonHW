# import rndm package for rndm choices
from random import randint
# import time module
import time


# Choices array
choices = ["Rock", "Paper", "Scissors"]

# Set the computer's choice
computer = choices[randint(0,2)]

# set up game loop and other variables
player = False
pScore = 0
cScore = 0

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
	
	elif player == "Rock":
		if computer == "Paper":
			print("You lose!", computer, "Covers", player, "\n")
			cScore = cScore + 1
		else:
			print("You win!", player, "Smashes", computer, "\n")
			pScore = pScore + 1

	elif player == "Paper":
		if computer == "Scissors":
			print("You lose!", computer, "Cuts", player, "\n")
			cScore = cScore + 1
		else:
			print("You win!", player, "Covers", computer, "\n")
			pScore = pScore + 1

	elif player == "Scissors":
		if computer == "Rock":
			print("You lose!", computer, "Smashes", player, "\n")
			cScore = cScore + 1
		else:
			print("You win!", player, "Cuts", computer, "\n")
			pScore = pScore + 1
	else:
		print("That's not a valid choice")
		

	#Show Score and response
	print("Player: ", pScore, "|| Computer: ", cScore, "\n")
	
	if cScore - pScore >= 7:
		print('Computer: "I am the King" \n')
	elif cScore - pScore >= 5:
		print('Computer: "You suck at this" \n')
	elif cScore - pScore > 3:
		print('Computer: "I am not even trying" \n')
	elif cScore - pScore == 3 :
		print('Computer: "This is easy" \n')
	elif cScore - pScore >= 1:
		print('Computer: "Nice! Let us go again" \n')
	elif cScore - pScore == 0:
		print('Computer: "We are tied" \n')
	elif cScore - pScore <= -7:
		print('Computer: "You are the King" \n')
	elif cScore - pScore <= -5:
		print('Computer: "You rock at this" \n')
	elif cScore - pScore < -3:
		print('Computer: "You are pretty good" \n')
	elif cScore - pScore == -3 :
		print('Computer: "This is hard" \n')
	elif cScore - pScore <= -1:
		print('Computer: "Damn! Let us go again" \n')

	player = False
	computer = choices[randint(0,2)]


