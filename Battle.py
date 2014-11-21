#coding: utf-8
import os, random, time, sys

#First image
space = """
.    .        .      .             . .     .        .          .          .
         .                 .                    .                .
  .               A long time ago in a galaxy far, far away...   .
     .               .           .               .        .             .
     .      .            .                 .                                .
 .      .         .         .   . :::::+::::...      .          .         .
     .         .      .    ..::.:::+++++:::+++++:+::.    .     .
                        .:.  ..:+:..+|||+..::|+|+||++|:.             .     .
            .   .    :::....:::::::::++||||O||O#OO|OOO|+|:.    .
.      .      .    .:..:..::+||OO#|#|OOO+|O||####OO###O+:+|+               .
                 .:...:+||O####O##||+|OO|||O#####O#O||OO|++||:     .    .
  .             ..::||+++|+++++|+::|+++++O#O|OO|||+++..:OOOOO|+  .         .
     .   .     +++||++:.:++:..+#|. ::::++|+++||++O##O+:.++|||#O+    .
.           . ++++++++...:+:+:.:+: ::..+|OO++O|########|++++||##+            .
  .       .  :::+++|O+||+::++++:::+:::+++::+|+O###########OO|:+OO       .  .
     .       +:+++|OO+|||O:+:::::.. .||O#OOO||O||#@###@######:+|O|  .
 .          ::+:++|+|O+|||++|++|:::+O#######O######O@############O
          . ++++: .+OO###O++++++|OO++|O#@@@####@##################+         .
      .     ::::::::::::::::::::++|O+..+#|O@@@@#@###O|O#O##@#OO####     .
 .        . :. .:.:. .:.:.: +.::::::::  . +#:#@:#@@@#O||O#O@:###:#| .      .
                           `. .:.:.:.:. . :.:.:%::%%%:::::%::::%:::
.      .         .                            `.:.:.:.:   :.:.:.:.  .   .
           .		.	.	.	.	.               
      .
.          .        .		.	.	.		.    .   .
							.                                                               .
"""
galaxy = """
   .        .            .       .          .   .           .                .
    .     .          .                  .                               .      .
  .     .                                                        .
              .   A terrible civil war burns throughout the  .        .     .
                 galaxy: a rag-tag group of freedom fighters   .  .
     .       .  has risen from beneath the dark shadow of the            .
.        .     evil monster the Galactic Empire has become.                  .
   .             Imperial  forces  have  instituted  a reign of   .      .
             terror,  and every  weapon in its arsenal has  been
          . turned upon the Rebels  and  their  allies:  tyranny, .   .
   .       oppression, vast fleets, overwhelming armies, and fear.        .  .
.      .  Fear  keeps  the  individual systems in line,  and is the   .
         prime motivator of the New Order.             .
    .      Outnumbered and outgunned,  the Rebellion burns across the   .    .
.      vast reaches of space and a thousand-thousand worlds, with only     .
    . their great courage - and the mystical power known as the Force -
     flaming a fire of hope.                                    .
       This is a  galaxy  of wondrous aliens,  bizarre monsters,  strange   .
 . Droids, powerful weapons, great heroes, and terrible villains.  It is a
  galaxy of fantastic worlds,  magical devices, vast fleets, awesome machi-  .
 nery, terrible conflict, and unending hope.              .         .
.        .          .    .    .            .            .                   .
               .               ..       .       .   .             .
 .      .                  .
                     .              .       .                    .      .
"""

star = """
      ________________.  ___     .______  
     /                | /   \    |   _  \ 
    |   (-----|  |----`/  ^  \   |  |_)  | 
     \   \    |  |    /  /_\  \  |      / 
.-----)   |   |  |   /  _____  \ |  |\  \-------. 
|________/    |__|  /__/     \__\| _| `.________| 
 ____    __    ____  ___     .______    ________. 
 \   \  /  \  /   / /   \    |   _  \  /        | 
  \   \/    \/   / /  ^  \   |  |_)  ||   (-----` 
   \            / /  /_\  \  |      /  \   \ 
    \    /\    / /  _____  \ |  |\  \---)   | 
     \__/  \__/ /__/     \__\|__| `._______/  
"""
#Showing images
print space
time.sleep(4)
os.system("clear")
print galaxy
time.sleep(15)
os.system("clear")


class singleplayer(object): 
	def __init__(self):
		pass
	def inicio(self):
		
		#App name
		app_name = "Battleship"
		#Autor
		app_author = "Sergio Merida"
		
		def clearScreen():
			os.system ("clear")


		#player boards
		player1_board = []
		player2_board = []
	
		#Name of players
		player1_name = ""
		player2_name = ""
		
		#Game conditions
		gameWon = False
		gameTurns = 1
		gameWinner = ""
		gameLoser = ""
		win = 0
		lose = 0
		player1won = False
		player2won = False

		#Position ships player1
		player1_ship_row = 9
		player1_ship_col = 9

		#Position ships player2
		player2_ship_row = 9
		player2_ship_col = 9
	
		#Board size
		boardColRow = 10

		#Ship
		shipChar = "S"

		#Ship hit
		firedChar = "X"
		missChar = "H"

		#Board
		boardChar = " "

		#Figlet
		hit =  """
    ____                           
   / __ )____  ____  ____ ___      
  / __  / __ \/ __ \/ __ `__ \     
 / /_/ / /_/ / /_/ / / / / / / _ _ 
/_____/\____/\____/_/ /_/ /_(_|_|_)
"""
		miss  = """
    __  __      __          __
   / / / /___ _/ /_  ____ _/ /
  / /_/ / __ `/ __ \/ __ `/ / 
 / __  / /_/ / / / / /_/ /_/  
/_/ /_/\__,_/_/ /_/\__,_(_) 
"""
		win2 = """
__  __                        _     
\ \/ /___  __  __   _      __(_)___ 
 \  / __ \/ / / /  | | /| / / / __ \ 
 / / /_/ / /_/ /   | |/ |/ / / / / /
/_/\____/\__,_/    |__/|__/_/_/ /_/ 
"""
		darth = """
	  _________
          III| |III
        IIIII| |IIIII
       IIIIII| |IIIIII
       IIIIII| |IIIIII
      IIIIIII| |IIIIIII
      IIIIIII\ /IIIIIII
     II (___)| |(___) II
    II  \    /D\    /  II
   II  \ \  /| |\  / /  II
  II    \_\/|| ||\/_/    II
 II     / O-------O \     II
II_____/   \|||||/   \_____II
      /               \ 

"""
		finish = """
             ___________
            | | |.-.| | |
       |\   |_.-" 8 "-._|   /|
       | \  `  SHIELD   '  / |
  \\-+-|  \               /  |-+-//
  |\\| |   \             / /|| |//|
  |__|\|   |\           /|| ||/|__|
   \_\ |   | \         / ||/ | /_/
       |   | |\       /| |   |
       |  .----------------. |
       | /__________________\|
       | \                  /|         "Use the Force, Luke!"
       |  `----------------' |
       |   | ||L/___\L|| |   |
       |   | |<=======>| |   |
       |   | |/       \| |   |
       |   | /* *      \ |   |
       |   |/* X *      \|   |
    __ |   /  * *        \   | __
   /_/ |  /               \  | \_\ 
  |  |/| /      _____      \ |\|  | 
  |//| |/     _/|___|\_     \| |\\| 
  //-+-      (/"|   |"\)      -+-\\ 
"""
		boom = """
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :| 
 _____.,-#%&$@%#&#~,._____  
"""

		#Ocean
		oceanChar = "O"
		
		#Print the name of the game and the author
		def gameLogo():
			print 
			print " Game " + str(app_name)
			print " Created by " + str(app_author)
			print
			print
		#Set a random position 
		def randomizePosition(board):
			return random.randint(0, len(player1_board) -1)

		#Set the options to print the player board
		def printPlayerBoard(board, row, col, boardChar):
			for i in board:
				print str(boardChar).join(i)
				board[row][col] = oceanChar

		#Set the options to print the opposite board
		def printPlayerOppositeBoard(board, boardChar):
			for i in board:
				print str(boardChar).join(i)
	
		#The turn of
		def acknowledge(player1name, player2name):
			clearScreen()
			gameLogo()
			print
			print
			return raw_input("It's the turn of " + str(player1name) + " (When you're ready press: 'ENTER')")

		#Press enter
		def acknowledgeFailure():
			return raw_input("To continue press enter...")
	
		#The messages 
		def displayMessage(errNumber, playername=""):
			message = {
			1: "Congrats you hit the space ship of " + str(playername),
			2: "Captain " + str(playername) + ", whe are in the space, so why are you targeting at the sun?",
			3: "Captain it's a trap you have already shoot there!",
			4: "Haha! You've missed",
			5: str(playername) + "'s board with your fired attempts!",
			6: "Your board with space ship location and " + str(playername) + "'s fired attempts!",
			7: "Congrats you sunk the space ship number 1 of " + str(playername),
			8: "You lack to sink the space ship number 1 of " + str(playername),
			9: "Congrats you sunk the space ship number 2 of " + str(playername),
			10: "You lack to sink the space ship number 2 of " + str(playername),
			11: "Uffff! That was close, the sith lord missed!"
		}
			return str(message[errNumber])


		# Appending the vowel oceanChar to the boards
		for i in range(boardColRow):
			player1_board.append([str(oceanChar)] * boardColRow)
			player2_board.append([str(oceanChar)] * boardColRow)

		#Setting the position of player1 ships
		check = False
		while check == False:
			#col of ship number 1 player1, ship of 2 spaces
			player1_ship_row1 = randomizePosition(player1_board)
			jugador1_fila2 = player1_ship_row1 + 1
			
			player1_ship_col1 = randomizePosition(player1_board)
			jugador1_columna2 = player1_ship_col1

			#row of ship number 2 player1, ship of 3 spaces
			player1_ship_row2 = randomizePosition(player1_board)
			player1_ship_r_part2 = player1_ship_row2
			player1_ship_r_part3 = player1_ship_row2

			player1_ship_col2 = randomizePosition(player1_board)
			player1_ship_c_part2 = player1_ship_col2 + 1	
			player1_ship_c_part3 = player1_ship_c_part2 + 1
			
			#Not bigger than the board
			if (jugador1_fila2 >= 10 or jugador1_columna2 >= 10) \
			or (player1_ship_r_part2 >= 10 or player1_ship_r_part3 >= 10) \
			or (player1_ship_c_part2 >= 10 or player1_ship_c_part3 >= 10):
				check = False

			#Not in the same position
			elif (player1_ship_row1 != player1_ship_row2 and jugador1_fila2 != player1_ship_row2) \
			and (player1_ship_row1 != player1_ship_r_part2 and jugador1_fila2 != player1_ship_r_part2) \
			and (player1_ship_row1 != player1_ship_r_part3 and jugador1_fila2 != player1_ship_r_part3) \
			and (player1_ship_col1 != player1_ship_col2 and jugador1_columna2 != player1_ship_col2) \
			and (player1_ship_col1 != player1_ship_c_part2 and jugador1_columna2 != player1_ship_c_part2) \
			and (player1_ship_col1 != player1_ship_c_part3 and jugador1_columna2 != player1_ship_c_part3): 
				check = True
				print "Player 1 ships"	
				print "Ship number 1"	
				print player1_ship_row1
				print player1_ship_col1
				print jugador1_fila2
				print jugador1_columna2
	
				print "***********"
				print "ship number 2"	
				print player1_ship_row2
				print player1_ship_col2
				print player1_ship_r_part2
				print player1_ship_c_part2
				print player1_ship_r_part3
				print player1_ship_c_part3
	
	

			#Setting the position of player2 ships
			check2 = False
			while check2 == False:
				#col of ship number 1 player2, ship of 2 spaces				
				player2_ship_row1 = randomizePosition(player2_board)
				jugador2_fila2 = player2_ship_row1 + 1
				
				player2_ship_col1 = randomizePosition(player2_board)
				jugador2_columna2 = player2_ship_col1

				#row of ship number 2 player1, ship of 3 spaces
				player2_ship_row2 = randomizePosition(player2_board)
				player2_ship_r_part2 = player2_ship_row2
				player2_ship_r_part3 = player2_ship_row2
			
				player2_ship_col2 = randomizePosition(player2_board)
				player2_ship_c_part2 = player2_ship_col2 + 1	
				player2_ship_c_part3 = player2_ship_c_part2 + 1
				
				#Not bigger than the board
				if (jugador2_fila2 >= 10 or jugador2_columna2 >= 10) \
				or (player2_ship_r_part2 >= 10 or player2_ship_r_part3 >= 10) \
				or (player2_ship_c_part2 >= 10 or player2_ship_c_part3 >= 10):
					check2 = False

				#Not in the same position
				elif (player2_ship_row1 != player2_ship_row2 and jugador2_fila2 != player2_ship_row2) \
				and (player2_ship_row1 != player2_ship_r_part2 and jugador2_fila2 != player2_ship_r_part2) \
				and (player2_ship_row1 != player2_ship_r_part3 and jugador2_fila2 != player2_ship_r_part3) \
				and (player2_ship_col1 != player2_ship_col2 and jugador2_columna2 != player2_ship_col2) \
				and (player2_ship_col1 != player2_ship_c_part2 and jugador2_columna2 != player2_ship_c_part2) \
				and (player2_ship_col1 != player2_ship_c_part3 and jugador2_columna2 != player2_ship_c_part3): 
					check2 = True		
					print "Player 2 ships"					
					print "Ship number 1"	
					print player2_ship_row1
					print player2_ship_col1
					print jugador2_fila2
					print jugador2_columna2
					print "***********"
					print "ship number 2"	
					print player2_ship_row2
					print player2_ship_r_part2
					print player2_ship_r_part3
					print player2_ship_col2
					print player2_ship_c_part2
					print player2_ship_c_part3
	

		#Clear the screen to make it fancy
		clearScreen()
		#print the name of author and program
		gameLogo()

		#Ask name of player 1 and player 2
		valida = False
		while (valida == False):
				
			player1_name = raw_input("Player One's Name: ")
			print "The sith lord its typing he's name"
			time.sleep(2)
			player2_name = "Darth Vader"
			print "Player Two Name: ", player2_name
			if len(player1_name)==0:
				print "How if you try again, maybe you can try whit your name"
				valida = False
			else:
				print "Perfect, your information been successfully added , enjoy the game."
				print "Loading information..."	
				time.sleep(3)

				valida = True


		#Look if hit a ship
		chec = False
		chec2 = False
		chec3 = False
		chec4 = False
		chec5 = False
		#Look if player 1 won	
		gana = False
		gana2 = False
		gana3 = False
		gana4 = False
		gana5 = False

		#Look if hit a ship
		twochec = False
		twochec2 = False
		twochec3 = False
		twochec4 = False
		twochec5 = False
		#Look if player 2 won
		dosGana = False
		dosGana2 = False
		dosGana3 = False
		dosGana4 = False		
		dosGana5 = False
		while 1:
			if gameTurns <= 1:
				acknowledge(player1_name, player2_name)
			"""
			Player One's Gaming Conditions
			"""
			clearScreen()
			gameLogo()
			print 
			print "Turn number: " + str(gameTurns), 
			print
			#If player hit one of the ships shows the position  			
			if gana == True and gana2 == True:
				print displayMessage(7, player2_name), "the space ship was in positions", "(", player2_ship_row1, ",", player2_ship_col1, ")", "(", jugador2_fila2, ",", jugador2_columna2, ")"   
			else:
				print displayMessage(8, player2_name)
			
			if gana3 == True and gana4 == True and gana5 == True:
				print displayMessage(9, player2_name), "the space ship was in positions", "(", player2_ship_row2, ",", player2_ship_col2, ")", "(", player2_ship_r_part2, ",", player2_ship_c_part2, ")", "(", player2_ship_r_part3, ",", player2_ship_c_part3, ")"
			else:
				print displayMessage(10, player2_name)

			print
			print "It's the turn of " + str(player1_name)
			print 
			print displayMessage(5, player2_name)

			# Print Player 2's Ocean without the ship on it
			printPlayerOppositeBoard(player2_board, boardChar)
			print
			print
			print displayMessage(6, player2_name)

			# Print Player 1's Ocean with ship on it
			printPlayerBoard(player1_board, player1_ship_row, player1_ship_col, boardChar)

			# General Game Conditions	
			print
			print
			valida = False
			while (valida == False):
				try:
					player1_guessedRow = input(str(player1_name) + " Guess Row: ")
					player1_guessedCol = input(str(player1_name) + " Guess Col: ")
					if player1_guessedRow < 0:
						print "Opss! attempts to place a number of 0 to 9"
						valida = False
					elif player1_guessedCol < 0:
						print "Opss! attempts to place a number of 0 to 9"
					else:
						valida = True
				except (ValueError, SyntaxError, NameError):
					valida = False
					print "Try to put a number, remember not allow letters or spaces."

			#Search if guessedRow and col hit a ship
			if player1_guessedRow == player2_ship_row1 and player1_guessedCol == player2_ship_col1:
				print hit
				print displayMessage(1, player2_name)								
				chec = True
				gana = True
		
			else:
				chec = False
				
			if player1_guessedRow == jugador2_fila2 and player1_guessedCol == jugador2_columna2:
				print hit				
				print displayMessage(1, player2_name)
				chec2 = True
				gana2 = True
				
			else:
				chec2 = False	

			if player1_guessedRow == player2_ship_row2 and player1_guessedCol == player2_ship_col2:
				print hit
				print displayMessage(1, player2_name)
				chec3 = True			
				gana3 = True
				
			else:
				chec3 = False

			if player1_guessedRow == player2_ship_r_part2 and player1_guessedCol == player2_ship_c_part2:
				print hit
				print displayMessage(1, player2_name)	
				chec4 = True				
				gana4 = True
			else:
				chec4 = False
			
			if player1_guessedRow == player2_ship_r_part3 and player1_guessedCol == player2_ship_c_part3:
				print hit
				print displayMessage(1, player2_name)
				chec5 = True
				gana5 = True
			else:
				chec5 = False
	
			#End of the game when sunk all the ships
			if gana == True and gana2 == True and gana3 == True and gana4 == True and gana5 == True:
				time.sleep(4)				
				clearScreen()
				print finish
				time.sleep(2)
				clearScreen()
				print boom
				time.sleep(2)
				print ""
				print "My young padawan " + str(player1_name) + " the force it's strong in you."
				print ""
				gameWon = True
				player1won = True
				gameWiner = str(player1_name)
				gameLoser = str(player2_name)
				break			
			else:
				if (player1_guessedRow < 0 or player1_guessedRow >= boardColRow) \
				or (player1_guessedCol < 0 or player1_guessedCol >= boardColRow):
					print
					print displayMessage(2)
					print
					acknowledgeFailure()
					acknowledge(player2_name, player2_name)
				elif player2_board[player1_guessedRow][player1_guessedCol] == str(firedChar) \
				or player2_board[player1_guessedRow][player1_guessedCol] == str(missChar):
					print
					print displayMessage(3)
					print
					acknowledgeFailure()
					acknowledge(player2_name, player2_name)
				else:
					if chec == True or chec2 == True or chec3 == True or chec4 == True or chec5 == True:
						player2_board[player1_guessedRow][player1_guessedCol] = str(missChar)
						
					else:	
						print miss
						print displayMessage(4)				
						player2_board[player1_guessedRow][player1_guessedCol] = str(firedChar)
					acknowledgeFailure()					
					acknowledge(player2_name, player2_name)
			"""
			Player Two's Gaming Conditions
			"""
			clearScreen()
			gameLogo()
			print
			print "Number of turns played: " + str(gameTurns)
			print
			if dosGana == True and dosGana2 == True:
				print displayMessage(7, player1_name), "The space ship position was", "(", player1_ship_row1, ",", player1_ship_col1, ")", "(", jugador1_fila2, ",", jugador1_columna2, ")"   
			else:
				print displayMessage(8, player1_name)
			
			if dosGana3 == True and dosGana4 == True and dosGana5 == True:
				print displayMessage(9, player1_name), "the space ship was in positions", "(", player1_ship_row2, ",", player1_ship_col2, ")", "(", player1_ship_r_part2, ",", player1_ship_c_part2, ")", "(", player1_ship_r_part3, ",", player1_ship_c_part3, ")"
			else:
				print displayMessage(10, player1_name)
			print
			print "It's the turn of " + str(player2_name)
			print

			print displayMessage(5, player1_name)
			# Print Player 1's Ocean without the ship on it
			printPlayerOppositeBoard(player1_board, boardChar)
			print
			print
			print displayMessage(6, player1_name)

			# Print Player 2's Ocean with ship on it
			printPlayerBoard(player2_board, player2_ship_row, player2_ship_col, boardChar)
			
			# General Game Conditions
			print
			print
			valida = False
			while (valida == False):
				try:	
					player2_guessedRow = random.randint(0, len(player1_board) -1)
					print player2_name, " Guess row: ", player2_guessedRow
					player2_guessedCol = random.randint(0, len(player1_board) -1)
					print player2_name, " Guess row: ", player2_guessedCol
					if player2_guessedRow < 0:
						print "Opss! attempts to place a number of 0 to 9"
						valida = False
					elif player2_guessedCol < 0:
						print "Opss! attempts to place a number of 0 to 9"
					else:
						valida = True
				except (ValueError, SyntaxError, NameError):
					valida = False
					print "Try to put a number, remember not allow letters or spaces."
			#Check if he hit
			if player2_guessedRow == player1_ship_row1 and player2_guessedCol == player1_ship_col1:
				print hit
				print displayMessage(1, player1_name)
				dosGana = True
				twochec = True
				
			else:
				twochec = False

			if player2_guessedRow == jugador1_fila2 and player2_guessedCol == jugador1_columna2:
				print hit
				print displayMessage(1, player1_name)
				dosGana2 = True
				twochec2 = True
				
			else:
				twochec2 = False

			if player2_guessedRow == player1_ship_row2 and player2_guessedCol == player1_ship_col2:
				print hit
				print displayMessage(1, player1_name)
				dosGana3 = True
				twochec3 = True
				
			else:
				twochec3 = False

			if player2_guessedRow == player1_ship_r_part2 and player2_guessedCol == player1_ship_c_part2:
				print hit
				print displayMessage(1, player1_name)
				dosGana4 = True
				twochec4 = True
				
			else:
				twochec4 = False

			if player2_guessedRow == player1_ship_r_part3 and player2_guessedCol == player1_ship_c_part3:
				print hit
				print displayMessage(1, player1_name)
				dosGana5 = True
				twochec5 = True
				
			else:
				twochec5 = False
			#If he won
			if dosGana == True and dosGana2 == True and dosGana3 == True and dosGana4 == True and dosGana5 == True:
				time.sleep(2)				
				clearScreen()
				print "Something happened"
				time.sleep(2)
				print ""
				print ""
				gameWon = True
				player2won = True
				gameWiner = str(player2_name)
				gameLoser = str(player1_name)
				break
			else:
				if (player2_guessedRow < 0 or player2_guessedRow >= boardColRow) \
				or (player2_guessedCol < 0 or player2_guessedCol >= boardColRow):
					print
					print displayMessage(2)
					print
					acknowledgeFailure()
					acknowledge(player1_name, player1_name)
				elif player1_board[player2_guessedRow][player2_guessedCol] == str(firedChar) \
				or player1_board[player2_guessedRow][player2_guessedCol] == str(missChar):
					print
					print displayMessage(3)
					print
					acknowledgeFailure()
					acknowledge(player1_name, player1_name)
				else:
					if twochec == True or twochec2 == True or twochec3 == True or twochec4 == True or twochec5 == True:
						player1_board[player2_guessedRow][player2_guessedCol] = str(missChar)
						
					else:	
						print						
						print displayMessage(11)				
						player1_board[player2_guessedRow][player2_guessedCol] = str(firedChar)
					acknowledgeFailure()					
					acknowledge(player1_name, player1_name)
				gameTurns += 1

		if gameWon:
			#Message of congratulations when one of the two players sunk all the opposite ships
			if gameWinner == player2_name:
				print str(player1_name) + "my young padawan you have been defeated by the dark side of the force."
				print darth
				print "Hahaha! You underestimate the power of the dark side"
				print
				print "The space ship number 1 of Darth Vader was in positions", "(", player2_ship_row1, ",", player2_ship_col1, ")", "(", jugador2_fila2, ",", jugador2_columna2, ")"
				print "The space ship number 2 of Darth Vader was in positions", "(", player2_ship_row2, ",", player2_ship_col2, ")", "(", player2_ship_r_part2, ",", player2_ship_c_part2, ")", "(", player2_ship_r_part3, ",", player2_ship_c_part3, ")"
				print "Train yourself to let go of everything you fear to lose."
				print
			else: 				
				print "Congratulations" + str(gameWinner) + " for shooting down " + str(gameLoser) + "'s space ships! in " + str(gameTurns) + " turns!"
				print			
				print win2
				print
				print "Powerful you have become."
				print
				print

			#Return to the menu
			respuesta = 0
			while (respuesta==0):
				try:	
					time.sleep(4)			
					a = raw_input ("Do you want to keep playing? 1.Yes / 2.No: ")
					b = a.lower()
					if b == "si" or b == "1":
						respuesta = 1
					elif b == "no" or b == "2":
						clearScreen()
						print """
	          .--.
	::\`--._,'.::.`._.--'/:::
	::::.  ` __::__ '  .:::::
	::::::-:.`'..`'.:-:::::::
	::::::::\ `--' /:::::::::
	"""
						print """
If you end your training now, if you choose the quick and easy path as Vader did, you will become an agent of evil.
PATIENCE YOU MUST HAVE my young padawan keep practicing.
"""
						#Sure
						time.sleep(4)
						sure = raw_input ("Are you really sure you want to exit? 1.Yes / 2.No: ")
						sures = sure.lower()
						if sures == "si" or sures == "1":
							clearScreen()
							print "Then may the Force be with you."
							print 
							print star
							sys.exit(0)
						elif sures == "no" or sures == "2":
							respuesta = 1
						else:
							print "You must enter a valid option, 1 or yes/ 2 or no"	
					else:
						print "You must enter a valid option, 1 or yes/ 2 or no"
				except (SyntaxError):
					print "How if you try without spaces or signs"


class multiplayer(object): 
	def __init__(self):
		pass
	def inicio(self):
		
		#App name
		app_name = "Battleship"
		#Autor
		app_author = "Sergio Merida"
		
		def clearScreen():
			os.system ("clear")


		#player boards
		player1_board = []
		player2_board = []
	
		#Name of players
		player1_name = ""
		player2_name = ""
		
		#Game conditions
		gameWon = False
		gameTurns = 1
		gameWinner = ""
		gameLoser = ""
		win = 0
		lose = 0
		player1won = False
		player2won = False

		#Position ships player1
		player1_ship_row = 9
		player1_ship_col = 9

		#Position ships player2
		player2_ship_row = 9
		player2_ship_col = 9
	
		#Board size
		boardColRow = 10

		#Ship
		shipChar = "S"

		#Ship hit
		firedChar = "X"
		missChar = "H"

		#Board
		boardChar = " "

		#Figlet
		hit =  """
    ____                           
   / __ )____  ____  ____ ___      
  / __  / __ \/ __ \/ __ `__ \     
 / /_/ / /_/ / /_/ / / / / / / _ _ 
/_____/\____/\____/_/ /_/ /_(_|_|_)
"""
		miss  = """
    __  __      __          __
   / / / /___ _/ /_  ____ _/ /
  / /_/ / __ `/ __ \/ __ `/ / 
 / __  / /_/ / / / / /_/ /_/  
/_/ /_/\__,_/_/ /_/\__,_(_) 
"""
		win2 = """
__  __                        _     
\ \/ /___  __  __   _      __(_)___ 
 \  / __ \/ / / /  | | /| / / / __ \ 
 / / /_/ / /_/ /   | |/ |/ / / / / /
/_/\____/\__,_/    |__/|__/_/_/ /_/ 
"""

		finish = """
             ___________
            | | |.-.| | |
       |\   |_.-" 8 "-._|   /|
       | \  `  SHIELD   '  / |
  \\-+-|  \               /  |-+-//
  |\\| |   \             / /|| |//|
  |__|\|   |\           /|| ||/|__|
   \_\ |   | \         / ||/ | /_/
       |   | |\       /| |   |
       |  .----------------. |
       | /__________________\|
       | \                  /|         "Use the Force, Luke!"
       |  `----------------' |
       |   | ||L/___\L|| |   |
       |   | |<=======>| |   |
       |   | |/       \| |   |
       |   | /* *      \ |   |
       |   |/* X *      \|   |
    __ |   /  * *        \   | __
   /_/ |  /               \  | \_\ 
  |  |/| /      _____      \ |\|  | 
  |//| |/     _/|___|\_     \| |\\| 
  //-+-      (/"|   |"\)      -+-\\ 
"""
		boom = """
     _.-^^---....,,--
 _--                  --_
<                        >)
|                         |
 \._                   _./
    ```--. . , ; .--'''
          | |   |
       .-=||  | |=-.
       `-=#$%&%$#=-'
          | ;  :| 
 _____.,-#%&$@%#&#~,._____  
"""


		#Ocean
		oceanChar = "O"
		
		#Game def's
		def gameLogo():
			print 
			print " Game " + str(app_name)
			print " Created by " + str(app_author)
			print
			print
	
		def randomizePosition(board):
			return random.randint(0, len(player1_board) -1)

		def printPlayerBoard(board, row, col, boardChar):
			for i in board:
				print str(boardChar).join(i)
				board[row][col] = oceanChar

		def printPlayerOppositeBoard(board, boardChar):
			for i in board:
				print str(boardChar).join(i)
	
		def acknowledge(player1name, player2name):
			clearScreen()
			gameLogo()
			print
			print
			return raw_input("It's the turn of " + str(player1name) + " (When you're ready press: 'ENTER')")

		def acknowledgeFailure():
			return raw_input("To continue press enter...")
	
		def displayMessage(errNumber, playername=""):
			message = {
			1: "Congrats you hit the space ship of " + str(playername),
			2: "Captain " + str(playername) + ", whe are in the space, so why are you targeting at the sun?",
			3: "Captain it's a trap you have already shoot there!",
			4: "Haha! You've missed",
			5: str(playername) + "'s board with your fired attempts!",
			6: "Your board with space ship location and " + str(playername) + "'s fired attempts!",
			7: "Congrats you sunk the space ship number 1 of " + str(playername),
			8: "You lack to sink the space ship number 1 of " + str(playername),
			9: "Congrats you sunk the space ship number 2 of " + str(playername),
			10: "You lack to sink the space ship number 2 of " + str(playername),
			
		}
			return str(message[errNumber])


		#
		for i in range(boardColRow):
			player1_board.append([str(oceanChar)] * boardColRow)
			player2_board.append([str(oceanChar)] * boardColRow)

		#Colocando las posiciones de los barcos del jugador 1
		#Setting the position of player1 ships
		check = False
		while check == False:
			#col of ship number 1 player1, ship of 2 spaces
			player1_ship_row1 = randomizePosition(player1_board)
			jugador1_fila2 = player1_ship_row1 + 1
			
			player1_ship_col1 = randomizePosition(player1_board)
			jugador1_columna2 = player1_ship_col1

			#row of ship number 2 player1, ship of 3 spaces
			player1_ship_row2 = randomizePosition(player1_board)
			player1_ship_r_part2 = player1_ship_row2
			player1_ship_r_part3 = player1_ship_row2

			player1_ship_col2 = randomizePosition(player1_board)
			player1_ship_c_part2 = player1_ship_col2 + 1	
			player1_ship_c_part3 = player1_ship_c_part2 + 1
			
			#Not bigger than the board
			if (jugador1_fila2 >= 10 or jugador1_columna2 >= 10) \
			or (player1_ship_r_part2 >= 10 or player1_ship_r_part3 >= 10) \
			or (player1_ship_c_part2 >= 10 or player1_ship_c_part3 >= 10):
				check = False

			#Not in the same position
			elif (player1_ship_row1 != player1_ship_row2 and jugador1_fila2 != player1_ship_row2) \
			and (player1_ship_row1 != player1_ship_r_part2 and jugador1_fila2 != player1_ship_r_part2) \
			and (player1_ship_row1 != player1_ship_r_part3 and jugador1_fila2 != player1_ship_r_part3) \
			and (player1_ship_col1 != player1_ship_col2 and jugador1_columna2 != player1_ship_col2) \
			and (player1_ship_col1 != player1_ship_c_part2 and jugador1_columna2 != player1_ship_c_part2) \
			and (player1_ship_col1 != player1_ship_c_part3 and jugador1_columna2 != player1_ship_c_part3): 
				check = True
				print "Player 1 ships"	
				print "Ship number 1"	
				print player1_ship_row1
				print player1_ship_col1
				print jugador1_fila2
				print jugador1_columna2
	
				print "***********"
				print "ship number 2"	
				print player1_ship_row2
				print player1_ship_col2
				print player1_ship_r_part2
				print player1_ship_c_part2
				print player1_ship_r_part3
				print player1_ship_c_part3
	
	

			#Setting the position of player2 ships
			check2 = False
			while check2 == False:
				#col of ship number 1 player2, ship of 2 spaces				
				player2_ship_row1 = randomizePosition(player2_board)
				jugador2_fila2 = player2_ship_row1 + 1
				
				player2_ship_col1 = randomizePosition(player2_board)
				jugador2_columna2 = player2_ship_col1

				#row of ship number 2 player1, ship of 3 spaces
				player2_ship_row2 = randomizePosition(player2_board)
				player2_ship_r_part2 = player2_ship_row2
				player2_ship_r_part3 = player2_ship_row2
			
				player2_ship_col2 = randomizePosition(player2_board)
				player2_ship_c_part2 = player2_ship_col2 + 1	
				player2_ship_c_part3 = player2_ship_c_part2 + 1
				
				#Not bigger than the board
				if (jugador2_fila2 >= 10 or jugador2_columna2 >= 10) \
				or (player2_ship_r_part2 >= 10 or player2_ship_r_part3 >= 10) \
				or (player2_ship_c_part2 >= 10 or player2_ship_c_part3 >= 10):
					check2 = False

				#Not in the same position
				elif (player2_ship_row1 != player2_ship_row2 and jugador2_fila2 != player2_ship_row2) \
				and (player2_ship_row1 != player2_ship_r_part2 and jugador2_fila2 != player2_ship_r_part2) \
				and (player2_ship_row1 != player2_ship_r_part3 and jugador2_fila2 != player2_ship_r_part3) \
				and (player2_ship_col1 != player2_ship_col2 and jugador2_columna2 != player2_ship_col2) \
				and (player2_ship_col1 != player2_ship_c_part2 and jugador2_columna2 != player2_ship_c_part2) \
				and (player2_ship_col1 != player2_ship_c_part3 and jugador2_columna2 != player2_ship_c_part3): 
					check2 = True		
					print "Player 2 ships"					
					print "Ship number 1"	
					print player2_ship_row1
					print player2_ship_col1
					print jugador2_fila2
					print jugador2_columna2
					print "***********"
					print "ship number 2"	
					print player2_ship_row2
					print player2_ship_r_part2
					print player2_ship_r_part3
					print player2_ship_col2
					print player2_ship_c_part2
					print player2_ship_c_part3
	

		#Clear the screen to make it fancy
		clearScreen()
		#print the name of author and program
		gameLogo()

		#Ask name of player 1 and player 2
		valida = False
		while (valida == False):
			player1_name = raw_input("Player One's Name: ")
			player2_name = raw_input("Player Two's Name: ")
			if (len(player1_name)==0 or len(player2_name)==0):
				print "How if you try again, maybe you can try whit your name"
				valida = False
			else:
				print "Perfect, your information been successfully added , enjoy the game."
				print "Loading information..."		
				time.sleep(3)
				valida = True


		#Look if hit a ship
		chec = False
		chec2 = False
		chec3 = False
		chec4 = False
		chec5 = False
		#Look if player 1 won	
		gana = False
		gana2 = False
		gana3 = False
		gana4 = False
		gana5 = False

		#Look if hit a ship
		twochec = False
		twochec2 = False
		twochec3 = False
		twochec4 = False
		twochec5 = False
		#Look if player 2 won
		dosGana = False
		dosGana2 = False
		dosGana3 = False
		dosGana4 = False		
		dosGana5 = False
		while 1:
			if gameTurns <= 1:
				acknowledge(player1_name, player2_name)
			"""
			Player One's Gaming Conditions
			"""
			clearScreen()
			gameLogo()
			print
			print "Turn number: " + str(gameTurns)
			print 			
			if gana == True and gana2 == True:
				print displayMessage(7, player2_name), "the space ship position was", "(", player2_ship_row1, ",", player2_ship_col1, ")", "(", jugador2_fila2, ",", jugador2_columna2, ")"   
			else:
				print displayMessage(8, player2_name)
			
			if gana3 == True and gana4 == True and gana5 == True:
				print displayMessage(9, player2_name), "the space ship was in positions", "(", player2_ship_row2, ",", player2_ship_col2, ")", "(", player2_ship_r_part2, ",", player2_ship_c_part2, ")", "(", player2_ship_r_part3, ",", player2_ship_c_part3, ")"
			else:
				print displayMessage(10, player2_name)

			print
			print "It's the turn of " + str(player1_name)
			print
			print displayMessage(5, player2_name)

			# Print Player 2's Ocean without the ship on it
			printPlayerOppositeBoard(player2_board, boardChar)
			print
			print
			print displayMessage(6, player2_name)

			# Print Player 1's Ocean with ship on it
			printPlayerBoard(player1_board, player1_ship_row, player1_ship_col, boardChar)

			# General Game Conditions	
			print
			print
			valida = False
			while (valida == False):
				try:
					player1_guessedRow = input(str(player1_name) + " Guess Row: ")
					player1_guessedCol = input(str(player1_name) + " Guess Col: ")
					if player1_guessedRow < 0:
						print "Opss! attempts to place a number of 0 to 9"
						valida = False
					elif player1_guessedCol < 0:
						print "Opss! attempts to place a number of 0 to 9"
					else:
						valida = True
				except (ValueError, SyntaxError, NameError):
					valida = False
					print "Try to put a number, remember not allow letters or spaces."

			#Search if guessedRow and col hit a ship
			if player1_guessedRow == player2_ship_row1 and player1_guessedCol == player2_ship_col1:
				print hit
				print displayMessage(1, player2_name)								
				chec = True
				gana = True
				
			else:
				chec = False
				
			if player1_guessedRow == jugador2_fila2 and player1_guessedCol == jugador2_columna2:
				print hit				
				print displayMessage(1, player2_name)
				chec2 = True
				gana2 = True
				
			else:
				chec2 = False	

			if player1_guessedRow == player2_ship_row2 and player1_guessedCol == player2_ship_col2:
				print hit
				print displayMessage(1, player2_name)
				chec3 = True			
				gana3 = True
				
			else:
				chec3 = False

			if player1_guessedRow == player2_ship_r_part2 and player1_guessedCol == player2_ship_c_part2:
				print hit
				print displayMessage(1, player2_name)	
				chec4 = True				
				gana4 = True
			else:
				chec4 = False
			
			if player1_guessedRow == player2_ship_r_part3 and player1_guessedCol == player2_ship_c_part3:
				print hit
				print displayMessage(1, player2_name)
				chec5 = True
				gana5 = True
			else:
				chec5 = False
	
			#End of the game when sunk all the ships
			if gana == True and gana2 == True and gana3 == True and gana4 == True and gana5 == True:
				time.sleep(4)				
				clearScreen()
				print finish
				time.sleep(2)
				clearScreen()
				print boom
				time.sleep(2)
				print ""
				print "My young padawan " + str(player1_name) + " the force it's strong in you."
				print ""
				gameWon = True
				player1won = True
				gameWiner = str(player1_name)
				gameLoser = str(player2_name)
				break			
			else:
				if (player1_guessedRow < 0 or player1_guessedRow >= boardColRow) \
				or (player1_guessedCol < 0 or player1_guessedCol >= boardColRow):
					print
					print displayMessage(2)
					print
					acknowledgeFailure()
					acknowledge(player2_name, player2_name)
				elif player2_board[player1_guessedRow][player1_guessedCol] == str(firedChar) \
				or player2_board[player1_guessedRow][player1_guessedCol] == str(missChar):
					print
					print displayMessage(3)
					print
					acknowledgeFailure()
					acknowledge(player2_name, player2_name)
				else:
					if chec == True or chec2 == True or chec3 == True or chec4 == True or chec5 == True:
						player2_board[player1_guessedRow][player1_guessedCol] = str(missChar)
						
					else:	
						print miss
						print displayMessage(4)				
						player2_board[player1_guessedRow][player1_guessedCol] = str(firedChar)
					acknowledgeFailure()					
					acknowledge(player2_name, player2_name)


			"""
			Player Two's Gaming Conditions
			"""
			clearScreen()
			gameLogo()
			print
			print "Number of turns played: " + str(gameTurns)
			print
			if dosGana == True and dosGana2 == True:
				print displayMessage(7, player1_name), "The space ship position was", "(", player1_ship_row1, ",", player1_ship_col1, ")", "(", jugador1_fila2, ",", jugador1_columna2, ")"   
			else:
				print displayMessage(8, player1_name)
			
			if dosGana3 == True and dosGana4 == True and dosGana5 == True:
				print displayMessage(9, player1_name), "The space ship position was", "(", player1_ship_row1, ",", player1_ship_col1, ")", "(", jugador1_fila2, ",", jugador1_columna2, ")"
			else:
				print displayMessage(10, player1_name)
			print
			print "It's the turn of " + str(player2_name)
			print

			print displayMessage(5, player1_name)
			# Print Player 1's Ocean without the ship on it
			printPlayerOppositeBoard(player1_board, boardChar)
			print
			print
			print displayMessage(6, player1_name)

			# Print Player 2's Ocean with ship on it
			printPlayerBoard(player2_board, player2_ship_row, player2_ship_col, boardChar)
			
			# General Game Conditions
			print
			print
			valida = False
			while (valida == False):
				try:	
					player2_guessedRow = input(str(player2_name) + " Guess Row: ")
					player2_guessedCol = input(str(player2_name) + " Guess Col: ")
					if player2_guessedRow < 0:
						print "Opss! attempts to place a number of 0 to 9"
						valida = False
					elif player2_guessedCol < 0:
						print "Opss! attempts to place a number of 0 to 9"
					else:
						#print "Numero ingresado exitosamente"
						valida = True
				except (ValueError, SyntaxError, NameError):
					valida = False
					print "Try to put a number, remember not allow letters or spaces."

			if player2_guessedRow == player1_ship_row1 and player2_guessedCol == player1_ship_col1:
				print hit
				print displayMessage(1, player1_name)
				dosGana = True
				twochec = True
				
			else:
				twochec = False

			if player2_guessedRow == jugador1_fila2 and player2_guessedCol == jugador1_columna2:
				print hit
				print displayMessage(1, player1_name)
				dosGana2 = True
				twochec2 = True
				
			else:
				twochec2 = False

			if player2_guessedRow == player1_ship_row2 and player2_guessedCol == player1_ship_col2:
				print hit
				print displayMessage(1, player1_name)
				dosGana3 = True
				twochec3 = True
				
			else:
				twochec3 = False

			if player2_guessedRow == player1_ship_r_part2 and player2_guessedCol == player1_ship_c_part2:
				print hit
				print displayMessage(1, player1_name)
				dosGana4 = True
				twochec4 = True
				
			else:
				twochec4 = False

			if player2_guessedRow == player1_ship_r_part3 and player2_guessedCol == player1_ship_c_part3:
				print hit
				print displayMessage(1, player1_name)
				dosGana5 = True
				twochec5 = True
				
			else:
				twochec5 = False
			
			if dosGana == True and dosGana2 == True and dosGana3 == True and dosGana4 == True and dosGana5 == True:
				time.sleep(4)				
				clearScreen()
				print finish
				time.sleep(2)
				clearScreen()
				print boom
				time.sleep(2)
				print ""
				print "My young padawan " + str(player1_name) + " the force it's strong in you."
				print ""
				gameWon = True
				player2won = True
				gameWiner = str(player2_name)
				gameLoser = str(player1_name)
				break
			else:
				if (player2_guessedRow < 0 or player2_guessedRow >= boardColRow) \
				or (player2_guessedCol < 0 or player2_guessedCol >= boardColRow):
					print
					print displayMessage(2)
					print
					acknowledgeFailure()
					acknowledge(player1_name, player1_name)
				elif player1_board[player2_guessedRow][player2_guessedCol] == str(firedChar) \
				or player1_board[player2_guessedRow][player2_guessedCol] == str(missChar):
					print
					print displayMessage(3)
					print
					acknowledgeFailure()
					acknowledge(player1_name, player1_name)
				else:
					if twochec == True or twochec2 == True or twochec3 == True or twochec4 == True or twochec5 == True:
						player1_board[player2_guessedRow][player2_guessedCol] = str(missChar)
						
					else:	
						print miss
						print displayMessage(4)					
						player1_board[player2_guessedRow][player2_guessedCol] = str(firedChar)
					acknowledgeFailure()					
					acknowledge(player1_name, player1_name)
				gameTurns += 1

		if gameWon:
			#Message of congratulations when one of the two players sunk all the opposite ships
			if gameWinner == player2_name:
				print "Congratulations" + str(gameWinner) + " for shooting down " + str(gameLoser) + "'s space ships! in " + str(gameTurns) + " turns!"
				print str(player1_name) + "my young padawan you have been defeated."
				print win2
				print
				print "The space ship number 1 was in positions", "(", player2_ship_row1, ",", player2_ship_col1, ")", "(", jugador2_fila2, ",", jugador2_columna2, ")"
				print "The space ship number 2 was in positions", "(", player2_ship_row2, ",", player2_ship_col2, ")", "(", player2_ship_r_part2, ",", player2_ship_c_part2, ")", "(", player2_ship_r_part3, ",", player2_ship_c_part3, ")"
				print "Train yourself to let go of everything you fear to lose."
				print
			else: 				
				print "Congratulations" + str(gameWinner) + " for shooting down " + str(gameLoser) + "'s space ships! in " + str(gameTurns) + " turns!"
				print str(player2_name) + "my young padawan you have been defeated."
				print win2		
				print 
				print "The space ship number 1 was in positions", "(", player1_ship_row1, ",", player1_ship_col1, ")", "(", jugador1_fila2, ",", jugador1_columna2, ")"
				print "The space ship number 2 was in positions", "(", player1_ship_row2, ",", player1_ship_col2, ")", "(", player1_ship_r_part2, ",", player1_ship_c_part2, ")", "(", player1_ship_r_part3, ",", player1_ship_c_part3, ")"
				print "Train yourself to let go of everything you fear to lose."

			respuesta = 0
			while (respuesta==0):
				try:	
					time.sleep(4)			
					a = raw_input ("Do you want to keep playing? 1.Yes / 2.No: ")
					b = a.lower()
					if b == "si" or b == "1":
						respuesta = 1
					elif b == "no" or b == "2":
						clearScreen()
						print """
	          .--.
	::\`--._,'.::.`._.--'/:::
	::::.  ` __::__ '  .:::::
	::::::-:.`'..`'.:-:::::::
	::::::::\ `--' /:::::::::
	"""
						print """
If you end your training now, if you choose the quick and easy path as Vader did, you will become an agent of evil.
PATIENCE YOU MUST HAVE my young padawan keep practicing.
"""
						sure = raw_input ("Are you really sure you want to exit? 1.Yes / 2.No: ")
						sures = sure.lower()
						if sures == "si" or sures == "1":
							clearScreen()
							print "Then may the Force be with you."
							print 
							print star
							sys.exit(0)
						elif sures == "no" or sures == "2":
							respuesta = 1
						else:
							print "You must enter a valid option, 1 or yes/ 2 or no"	
					else:
						print "You must enter a valid option, 1 or yes/ 2 or no"
				except (SyntaxError):
					print "How if you try without spaces or signs"

#Exit 
class exit(object):
	def __init__(self):
		pass
	def inicio(self):
		os.system ("clear")
		print star
		print
		print "Then may the Force be with you."
		print "Thanks for using our Battleship Star Wars edition, we hope you had fun."
		print ""
		sys.exit(0)

menu = {'2':multiplayer, '1':singleplayer, '3':exit}

#Menu and conditions of the menu
while True:
	valida = False
	while (valida == False):
		os.system ("clear")
		print star
		print
		print "Welcome to Battleship Star Wars edition"
		print """
These are the instuctions of Battleship game: 
1. You have two ships one of 2 spaces and other of 3 spaces positioned randomly.
2. You have to guess the row and col of the other player ship's and try to sunk all.
3. You can choose SinglePlayer or MultiPlayer.
So have fun, we hope you like the game. 			
"""
		print """
Make your choice (1-4) if you want:
	'1. Singleplayer'
	'2. Multiplayer'
	'3. Exit'
			"""
		try:
			opcion = raw_input("So what do you want to play: \n")
			if len(opcion)==0:
				print "It can't be empty, please try again"
				valida = False
			else:
				variable = menu[opcion]()
				print variable.inicio()
				valida = True
		except KeyError:
			print "I dont understand, please can you try again."
			valida = False

