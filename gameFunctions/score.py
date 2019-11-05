def showScore (cWin, cScore, pScore):
	#Show Score and response
	print("Player: ", pScore, "|| Computer: ", cScore, "\n")
	
	if cScore - pScore == 0:
		print('Computer: "We are tied" \n')
	elif cWin == True:
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
		else: 
			print('Computer: "Ok you are still winning. Let us go again" \n')
	else:		
		if cScore - pScore <= -7:
			print('Computer: "You are the King" \n')
		elif cScore - pScore <= -5:
			print('Computer: "You rock at this" \n')
		elif cScore - pScore < -3:
			print('Computer: "You are pretty good" \n')
		elif cScore - pScore == -3 :
			print('Computer: "This is hard" \n')
		elif cScore - pScore <= -1:
			print('Computer: "Damn! Let us go again" \n')
		else:
			print('Computer: "Ok but I am still winning" \n')