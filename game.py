# import rndm package for rndm choices
from random import randint

# Choices array
choices = ["rock", "paper", "scissors"]

# Set the computer's choice
computer = choices[randint(0,2)]

# set up game loop
player = False

while player == False:
	# set player to True
	player = input("choose rock, paper or scissors\n")

	print("computer chose ", computer, "\n" )
	print("player chose ", player, "\n" )

	if player == "quit":
		exit()
	elif computer == player:
		print("It's a Tie")


	player = False
	computer = choices[randint(0,2)]


