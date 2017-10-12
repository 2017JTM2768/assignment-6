###### this is the 2nd .py file ###########

####### write your code here ##########

##Initializing board with 0 values

Board = [0,0,0,0,0,0,0,0,0]

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
count = 0;	# Variable for tracking number of moves

while Board[i]!=0:
	
	
	
	if playerOneTurn :

       		print( "Player 1’s chance")
		Position = int(raw_input("Enter the position"))
		Number = int(raw_input("Enter the Board"))

		if (Number==1 or Number ==3 or Number == 5 or Number == 7 or Number == 9):
			Board[Position]=Number
			printBoard() # Printing Board if valid move
			count = count + 1 
		else :
			print("Enter Valid digits please")
			continue # going back to the start of while loop statements

## Constraining the >15 cases

		if ((int(Board[0])+int(Board[1]) >15 or (int(Board[1]+int(Board[2])  >15 \ #two element row addition
		    (int(Board[3])+int(Board[4]) >15 or (int(Board[4])+int(Board[5]) >15 \ #two element row addition
		    (int(Board[6])+int(Board[7]) >15 or (int(Board[7])+int(Board[8]) >15 \ #two element row addition
		    (int(Board[0])+int(Board[2]) >15 or (int(Board[3]+int(Board[5])  >15 or int (int(Board[6]+int(Board[8]) >15 \ #two element row addition
		    (int(Board[0])+int(Board[3]) >15 or (int(Board[3]+int(Board[6])  >15 \ #two element column addition 
		    (int(Board[1])+int(Board[4]) >15 or (int(Board[4])+int(Board[7]) >15 \ #two element column addition
		    (int(Board[2])+int(Board[5]) >15 or (int(Board[5])+int(Board[8]) >15 \ #two element column addition
		    (int(Board[0])+int(Board[6]) >15 or (int(Board[1]+int(Board[7])  >15 or (int(Board[2]+int(Board[8]) >15 \ #two element column addition
		    (int(Board[0])+int(Board[4]) >15 or (int(Board[4])+int(Board[8]) >15) \
		    (int(Board[2])+int(Board[4]) >15 or (int(Board[4])+int(Board[6]) >15)): # two element Diagonal additon
			if count < 10:
				print("Illegal Move")
				continue # going back to the start of while loop statements
			elif count ==9 and \
			     (int(Board[0])+int(Board[1])+int(Board[2]) =15 or (int(Board[3])+int(Board[4])+int(Board[5]) =15 or (int(Board[6])+int(Board[7])+int(Board[8]) =15 \ # Row Sum
		     	      int(Board[0])+int(Board[3])+int(Board[7]) =15 or (int(Board[1])+int(Board[4])+int(Board[7]) =15 or (int(Board[2])+int(Board[5])+int(Board[8]) =15 \ # Column Sum
		              int(Board[0])+int(Board[4])+int(Board[8]) =15 or (int(Board[2])+int(Board[4])+int(Board[6]) =15
				print
			
			
 	else :
        	print( "Player 2’s chance")

		Position = int(raw_input("Enter the position"))
		Number = int(raw_input("Enter the Board"))

		if (Number==2 or Number ==4 or Number == 6 or Number == 8):
			Board[Position]=Number
			printBoard() # Printing Board if valid move
			count = count + 1
		else :
			print("Enter Valid digits please")
			continue # going back to the start of while loop statements

## Constraining the >15 cases
		if ((int(Board[0])+int(Board[1]) >15 or (int(Board[1]+int(Board[2])  >15 \ #two element row addition
		    (int(Board[3])+int(Board[4]) >15 or (int(Board[4])+int(Board[5]) >15 \ #two element row addition
		    (int(Board[6])+int(Board[7]) >15 or (int(Board[7])+int(Board[8]) >15 \ #two element row addition
		    (int(Board[0])+int(Board[2]) >15 or (int(Board[3]+int(Board[5])  >15 or int (int(Board[6]+int(Board[8]) >15 \ #two element row addition
		    (int(Board[0])+int(Board[3]) >15 or (int(Board[3]+int(Board[6])  >15 \ #two element column addition 
		    (int(Board[1])+int(Board[4]) >15 or (int(Board[4])+int(Board[7]) >15 \ #two element column addition
		    (int(Board[2])+int(Board[5]) >15 or (int(Board[5])+int(Board[8]) >15 \ #two element column addition
		    (int(Board[0])+int(Board[6]) >15 or (int(Board[1]+int(Board[7])  >15 or (int(Board[2]+int(Board[8]) >15 \ #two element column addition
		    (int(Board[0])+int(Board[4]) >15 or (int(Board[4])+int(Board[8]) >15) \
		    (int(Board[2])+int(Board[4]) >15 or (int(Board[4])+int(Board[6]) >15)): # two element Diagonal additon
			if count < 10:
				print("Illegal Move")
				continue # going back to the start of while loop statements
			else

	playerOneTurn = not playerOneTurn
		

	
	

