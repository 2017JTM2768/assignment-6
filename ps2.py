###### this is the second .py file ###########

####### write your code here ##########

Board = []

## Defining board position range

for x in range (0, 9) :
    Board.append(str(x + 1))




## Board function

def printBoard() :
    print( '\n -----')
    print( '|' + Board[0] + '|' + Board[1] + '|' + Board[2] + '|')
    print( ' -----')
    print( '|' + Board[3] + '|' + Board[4] + '|' + Board[5] + '|')
    print( ' -----')
    print( '|' + Board[6] + '|' + Board[7] + '|' + Board[8] + '|')
    print( ' -----\n')

## Logic

playerOneTurn = True

while True:
	
	if playerOneTurn :
       		print( "Player 1’s chance")
 	else :
        	print( "Player 2’s chance")

	Number = int(raw_input("Enter the Board"))

	if (Number==1 or Number ==3 or Number == 5 or Number == 7 or Number == 9)
		

	
	

