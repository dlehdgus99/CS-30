''' 
Written By: Dong Hyun Lee
Description: This is a version of rock-paper-scissors where the computer cheats and always wins. 
			 pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
			 This will always return 'computer wins'.
Date : 10/10/2018
'''

def rpsCheat(pChoice):
    return (print('computer wins'))

''' 
Description: This is a version of rock-paper-scissors where the computer always chooses rock. 
			 pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
			 This will returns either 'person wins', 'computer wins', or 'tie game'.
'''

def rpsRock(pChoice):
	if (pChoice == 'paper'):
	    return (print('person wins'))
	elif (pChoice == 'scissors'):
	    return (print('computer wins'))
	else:
	    return (print('tie game'))

'''
Description: This is an implementation of rock-paper-scissors for two players.
			 pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
			 cChoice is the computer's choice of a move, with the same three possible values.
			 This will return either 'person wins', 'computer wins', or 'tie game'.
'''
def rps2(pChoice, cChoice):
	if (pChoice == 'paper' and cChoice == 'rock'):
	    return (print('person wins'))
	elif (pChoice =='rock' and cChoice == 'scissors' ):
	    return (print('person wins'))	
	elif (pChoice =='scissors' and cChoice == 'paper' ):
	    return (print('person wins'))
	elif (pChoice == cChoice):
	    return (print('tie game'))
	else:
	    return (print('computer wins'))

''' 
Description: This is an implementation of rock-paper-scissors where the computer chooses its move randomly.
			 pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
			 This will return either 'person wins', 'computer wins', or 'tie game'.
'''
from random import choice

def rpsRandom(pChoice):
	return(rps2(pChoice, choice(['rock', 'paper', 'scissors'])))






	
