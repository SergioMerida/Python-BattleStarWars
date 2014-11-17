#coding: utf-8
import os, random, time, sys

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

		#Position ships player1
		player1_ship_row = 0
		player1_ship_col = 0

		#Position ships player2
		player2_ship_row = 0
		player2_ship_col = 0
	
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
			1: "Congrats you hit the ship of " + str(playername),
			2: "Captain " + str(playername) + ", whe are in the ocean, so why are you targeting at land?",
			3: "Captain you have already shoot there!",
			4: "Haha! You've missed my battleship!",
			5: str(playername) + "'s board with your fired attempts!",
			6: "Your board with ship location and " + str(playername) + "'s fired attempts!",
			7: "Congrats you sunk the ship number 1 of " + str(playername),
			8: "You lack to sink the ship number 1 of " + str(playername),
			9: "Congrats you sunk the ship number 2 of " + str(playername),
			10: "You lack to sink the ship number 2 of " + str(playername),
			11: "Uffff! That was close, PC missed!"
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
			
			if player1won == True:
				print "You have defeat the PC in", win, "occasions."
			else:
				print "You have been defeated in", lose, "occasions."
				
			player1_name = raw_input("Player One's Name: ")
			print "Computer its typing he's name"
			time.sleep(2)
			player2_name = "PC"
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
			print "Turn number: " + str(gameTurns)
			print 			
			if gana == True and gana2 == True:
				print displayMessage(7, player2_name), "The ship position was", "(", player2_ship_row1, ",", player2_ship_col1, ")", "(", jugador2_fila2, ",", jugador2_columna2, ")"   
			else:
				print displayMessage(8, player2_name)
			
			if gana3 == True and gana4 == True and gana5 == True:
				print displayMessage(9, player2_name)
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
				print gana
			else:
				chec = False
				
			if player1_guessedRow == jugador2_fila2 and player1_guessedCol == jugador2_columna2:
				print hit				
				print displayMessage(1, player2_name)
				chec2 = True
				gana2 = True
				print gana2
			else:
				chec2 = False	

			if player1_guessedRow == player2_ship_row2 and player1_guessedCol == player2_ship_col2:
				print hit
				print displayMessage(1, player2_name)
				chec3 = True	
				comprueba = True		
				gana3 = True
				print gana3
			else:
				chec3 = False

			if player1_guessedRow == player2_ship_r_part2 and player1_guessedCol == player2_ship_c_part2:
				print hit
				print displayMessage(1, player2_name)	
				chec4 = True				
				gana4 = True
				print gana4
			else:
				chec4 = False
			
			if player1_guessedRow == player2_ship_r_part3 and player1_guessedCol == player2_ship_c_part3:
				print hit
				print displayMessage(1, player2_name)
				chec5 = True
				gana5 = True
				print gana5
			else:
				chec5 = False
	
			#End of the game when sunk all the ships
			if gana == True and gana2 == True and gana3 == True and gana4 == True and gana5 == True:
				print "Wujuuuu! dude you won, I'm so happy right now!!"
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
				print displayMessage(7, player1_name), "The ship position was", "(", player1_ship_row1, ",", player1_ship_col1, ")", "(", jugador1_fila2, ",", jugador1_columna2, ")"   
			else:
				print displayMessage(8, player1_name)
			
			if dosGana3 == True and dosGana4 == True and dosGana5 == True:
				print displayMessage(9, player1_name), "The ship position was", "(", player1_ship_row1, ",", player1_ship_col1, ")", "(", jugador1_fila2, ",", jugador1_columna2, ")"
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

			if player2_guessedRow == player1_ship_row and player2_guessedCol == player1_ship_col:
				print hit
				print displayMessage(1, player1_name)
				dosGana = True
				twochec = True
				print dosGana
			else:
				twochec = False

			if player2_guessedRow == jugador1_fila2 and player2_guessedCol == jugador1_columna2:
				print hit
				print displayMessage(1, player1_name)
				dosGana2 = True
				twochec2 = True
				print dosGana2
			else:
				twochec2 = False

			if player2_guessedRow == player1_ship_row2 and player2_guessedCol == player1_ship_col2:
				print hit
				print displayMessage(1, player1_name)
				dosGana3 = True
				twochec3 = True
				print dosGana3
			else:
				twochec3 = False

			if player2_guessedRow == player1_ship_r_part2 and player2_guessedCol == player1_ship_c_part2:
				print hit
				print displayMessage(1, player1_name)
				dosGana4 = True
				twochec4 = True
				print dosGana4
			else:
				twochec4 = False

			if player2_guessedRow == player1_ship_r_part3 and player2_guessedCol == player1_ship_c_part3:
				print hit
				print displayMessage(1, player1_name)
				dosGana5 = True
				twochec5 = True
				print dosGana5
			else:
				twochec5 = False
			
			if dosGana == True and dosGana2 == True and dosGana3 == True and dosGana4 == True and dosGana5 == True:
				print "Wujuuuu! dude you won, I'm so happy right now!!"
				print ""
				gameWon = True
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
			print "Congratulations " + str(gameWinner) + " for shooting down " + str(gameLoser) + "'s ship! in " + str(gameTurns) + " turns!"
			print win2
			print 
			if player1won == True:
				win += 1
				print "You have defeat me in ", win, "occasions, you got lucky."
			else:
				lose += 1
				print "Haha you have been defeated in ", lose, "occasions why you dont try another time maybe you can defeat me"

			respuesta = 0
			while (respuesta==0):
				try:				
					a = raw_input ("Do you want to return to the menu? 1.Yes / 2.No: ")
					b = a.lower()
					if b == "yes" or b == "1":
						respuesta = 1
					elif b == "no" or b == "2":
						sys.exit(0)
					else:
						print "You must enter a valid option, 1 or yes / 2 or no "
				except (SyntaxError):
					print "How if you try without spaces or signs"

class multiplayer(object): 
	def __init__(self):
		pass
	def inicio(self):
		
		# Nombre de la aplicación
		app_name = "Battleship"
		# Autor
		app_author = "Sergio Merida"
		
		def clearScreen():
			os.system ("clear")


		#Tableros de jugadores
		player1_board = []
		player2_board = []
	
		#Nombre de jugadores
		player1_name = ""
		player2_name = ""
		
		#Condiciones de juego
		gameWon = False
		gameTurns = 1
		gameWinner = ""
		gameLoser = ""

		#Posición de los barcos jugador 1
		player1_ship_row = 0
		player1_ship_col = 0

		#Posición de los barcos jugador 2
		player2_ship_row = 0
		player2_ship_col = 0
	
		#Tamaño de tablero
		boardColRow = 10

		#Barco
		shipChar = "S"

		#Barco impactado
		firedChar = "X"

		#Tablero
		boardChar = " "

		#Oceano
		oceanChar = "O"
		
		#
		def gameLogo():
			print 
			print " Game " + str(app_name)
			print " Created by " + str(app_author)
			print
			print
	
		def randomizePosition(board):
			return random.randint(0, len(player1_board) -1)

		def printPlayerBoard(board, row, col, boardChar, shipChar):
			board[row][col] = str(shipChar)
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
			1: "Congrats you sunk the ship of " + str(playername),
			2: "Captain " + str(playername) + ", whe are in the ocean, so why are you targeting at land?",
			3: "Captain ou have already shoot there!",
			4: str(playername) + ": Haha! You've missed my battleship!",
			5: str(playername) + "'s board with your fired attempts!",
			6: "Your board with ship location and " + str(playername) + "'s fired attempts!"
		}
			return str(message[errNumber])


		#
		for i in range(boardColRow):
			player1_board.append([str(oceanChar)] * boardColRow)
			player2_board.append([str(oceanChar)] * boardColRow)

		#Colocando las posiciones de los barcos del jugador 1
		check = False
		while check == False:
			player1_ship_row = randomizePosition(player1_board)
			jugador1_fila2 = player1_ship_row + 1
			#col of ship number 1 player1, ship of 2 spaces
			player1_ship_col = randomizePosition(player1_board)
			jugador1_columna2 = player1_ship_col

			#row of ship number 2 player1, ship of 3 spaces
			player1_ship_row2 = randomizePosition(player1_board)
			player1_ship_r_part2 = player1_ship_row2
			player1_ship_r_part3 = player1_ship_row2

			player1_ship_col2 = randomizePosition(player1_board)
			player1_ship_c_part2 = player1_ship_col2 + 1	
			player1_ship_c_part3 = player1_ship_c_part2 + 1

			if (jugador1_fila2 >= 10 or jugador1_columna2 >= 10) \
			or (player1_ship_r_part2 >= 10 or player1_ship_r_part3 >= 10) \
			or (player1_ship_c_part2 >= 10 or player1_ship_c_part3 >= 10):
				check = False

			elif (player1_ship_row != player1_ship_row2 and jugador1_fila2 != player1_ship_row2) \
			and (player1_ship_row != player1_ship_r_part2 and jugador1_fila2 != player1_ship_r_part2) \
			and (player1_ship_row != player1_ship_r_part3 and jugador1_fila2 != player1_ship_r_part3) \
			and (player1_ship_col != player1_ship_col2 and jugador1_columna2 != player1_ship_col2) \
			and (player1_ship_col != player1_ship_c_part2 and jugador1_columna2 != player1_ship_c_part2) \
			and (player1_ship_col != player1_ship_c_part3 and jugador1_columna2 != player1_ship_c_part3): 
				check = True		
				print "Ship number 1"	
				print player1_ship_row
				print player1_ship_col
				print jugador1_fila2
				print jugador1_columna2
	
				print "***********"
				print "ship number 2"	
				print player1_ship_row2
				print player1_ship_r_part2
				print player1_ship_r_part3
				print player1_ship_col2
				print player1_ship_c_part2
				print player1_ship_c_part3
	
	

			#Colocando las posiciones de los barcos del jugador 2
			check2 = False
			while check2 == False:
				player2_ship_row = randomizePosition(player2_board)
				jugador2_fila2 = player2_ship_row + 1
				#col of ship number 1 player2, ship of 2 spaces
				player2_ship_col = randomizePosition(player2_board)
				jugador2_columna2 = player2_ship_col

				#row of ship number 2 player1, ship of 3 spaces
				player2_ship_row2 = randomizePosition(player2_board)
				player2_ship_r_part2 = player2_ship_row2
				player2_ship_r_part3 = player2_ship_row2
			
				player2_ship_col2 = randomizePosition(player2_board)
				player2_ship_c_part2 = player2_ship_col2 + 1	
				player2_ship_c_part3 = player2_ship_c_part2 + 1

				if (jugador2_fila2 >= 10 or jugador2_columna2 >= 10) \
				or (player2_ship_r_part2 >= 10 or player2_ship_r_part3 >= 10) \
				or (player2_ship_c_part2 >= 10 or player2_ship_c_part3 >= 10):
					check2 = False

				elif (player2_ship_row != player2_ship_row2 and jugador2_fila2 != player2_ship_row2) \
				and (player2_ship_row != player2_ship_r_part2 and jugador2_fila2 != player2_ship_r_part2) \
				and (player2_ship_row != player2_ship_r_part3 and jugador2_fila2 != player2_ship_r_part3) \
				and (player2_ship_col != player2_ship_col2 and jugador2_columna2 != player2_ship_col2) \
				and (player2_ship_col != player2_ship_c_part2 and jugador2_columna2 != player2_ship_c_part2) \
				and (player2_ship_col != player2_ship_c_part3 and jugador2_columna2 != player2_ship_c_part3): 
					check2 = True		
					print "Ship number 1"	
					print player2_ship_row
					print player2_ship_col
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


		#Look if player 1 won
		gana = False
		gana2 = False
		gana3 = False
		gana4 = False
		gana5 = False

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
			print "Number of turns played: " + str(gameTurns)
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
			printPlayerBoard(player1_board, player1_ship_row, player1_ship_col, boardChar, shipChar)

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
						#print "Numero ingresado exitosamente"
						valida = True
				except (ValueError, SyntaxError, NameError):
					valida = False
					print "Try to put a number, remember not allow letters or spaces."

	
	
			if player1_guessedRow == player2_ship_row and player1_guessedCol == player2_ship_col:
				print displayMessage(1, player2_name)
				gana = True
				print gana
			if player1_guessedRow == jugador2_fila2 and player1_guessedCol == jugador2_columna2:
				print displayMessage(1, player2_name)
				gana2 = True
				print gana2
			if player1_guessedRow == player2_ship_row2 and player1_guessedCol == player2_ship_col2:
				print displayMessage(1, player2_name)	
				gana3 = True
				print gana3
			if player1_guessedRow == player2_ship_r_part2 and player1_guessedCol == player2_ship_c_part2:
				print displayMessage(1, player2_name)	
				gana4 = True
				print gana4
			if player1_guessedRow == player2_ship_r_part3 and player1_guessedCol == player2_ship_c_part3:
				print displayMessage(1, player2_name)	
				gana5 = True
				print gana5
			if gana == True and gana2 == True and gana3 == True and gana4 == True and gana5 == True:
				print "Wujuuuu! dude you won, I'm so happy right now!!"
				print ""
				gameWon = True
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
				elif player2_board[player1_guessedRow][player1_guessedCol] == str(firedChar):
					print
					print displayMessage(3)
					print
					acknowledgeFailure()
					acknowledge(player2_name, player2_name)
				else:
					acknowledgeFailure()
					player2_board[player1_guessedRow][player1_guessedCol] = str(firedChar)
					acknowledge(player2_name, player2_name)
			"""
			Player Two's Gaming Conditions
			"""
			clearScreen()
			gameLogo()
			print
			print "Number of turns played: " + str(gameTurns)
			print
			print "It's the turn of " + str(player2_name)
			print

			print displayMessage(5, player1_name)
			# Print Player 2's Ocean without the ship on it
			printPlayerOppositeBoard(player1_board, boardChar)
			print
			print
			print displayMessage(6, player1_name)

			# Print Player 1's Ocean with ship on it
			printPlayerBoard(player2_board, player2_ship_row, player2_ship_col, boardChar, shipChar)
			
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

			if player2_guessedRow == player1_ship_row and player2_guessedCol == player1_ship_col:
				print displayMessage(1, player1_name)
				dosGana = True
				print gana
			if player2_guessedRow == jugador1_fila2 and player2_guessedCol == jugador1_columna2:
				print displayMessage(1, player1_name)
				dosGana2 = True
				print gana
			if player2_guessedRow == player1_ship_row2 and player2_guessedCol == player1_ship_col2:
				print displayMessage(1, player1_name)	
				dosGana3 = True
				print gana
			if player2_guessedRow == player1_ship_r_part2 and player2_guessedCol == player1_ship_c_part2:
				print displayMessage(1, player2_name)	
				dosGana4 = True
				print gana4
			if player2_guessedRow == player1_ship_r_part3 and player2_guessedCol == player1_ship_c_part3:
				print displayMessage(1, player2_name)	
				dosGana5 = True
				print gana5

			if dosGana == True and dosGana2 == True and dosGana3 == True and dosGana4 == True and dosGana5 == True:
				print "Wujuuuu! dude you won, I'm so happy right now!!"
				print ""
				gameWon = True
				gameWiner = str(player1_name)
				gameLoser = str(player2_name)
				break
			else:
				if (player2_guessedRow < 0 or player2_guessedRow >= boardColRow) \
				or (player2_guessedCol < 0 or player2_guessedCol >= boardColRow):
					print
					print displayMessage(2)
					print
					acknowledgeFailure()
					acknowledge(player1_name, player1_name)
				elif player1_board[player2_guessedRow][player2_guessedCol] == str(firedChar):
					print
					print displayMessage(3)
					print
					acknowledgeFailure()
					acknowledge(player1_name, player1_name)
				else:
					acknowledgeFailure()
					player1_board[player2_guessedRow][player2_guessedCol] = str(firedChar)
					acknowledge(player1_name, player1_name)
				gameTurns += 1

		if gameWon:
			#Message of congratulations when one of the two players sunk all the opposite ships
			print "Congratulations " + str(gameWinner) + " for shooting down " + str(gameLoser) + "'s ship! in " + str(gameTurns) + " turns!"
			print

			respuesta = 0
			while (respuesta==0):
				try:				
					a = raw_input ("Do you want to return to the menu? 1.Yes / 2.No: ")
					b = a.lower()
					if b == "si" or b == "1":
						respuesta = 1
					elif b == "no" or b == "2":
						sys.exit(0)
					else:
						print "You must enter a valid option, 1 or yes/ 2 or no"
				except (SyntaxError):
					print "How if you try without spaces or signs"

#Exit 
class exit(object):
	def __init__(self):
		pass
	def inicio(self):
		print "Thanks for using our battleship game, we hope you had fun."
		print ""
		sys.exit(0)

class instructions(object):
	def __init__(self):
		pass
	def inicio(self):		
		print """
These are the instuctions of Battleship game: 
1. You have two ships one of 2 spaces and other of 3 spaces positioned randomly.
2. You have to guess the row and col of the other player ship's and try to sunk all.
3. You can choose SinglePlayer or MultiPlayer.
So have fun, we hope you like the game. 			
"""

menu = {'2':multiplayer, '1':singleplayer, '3':instructions, '4':exit}

#Menu and conditions of the menu
while True:
	valida = False
	while (valida == False):
		os.system ("clear")
		print "Welcome to Battleship the Game"
		print """
Make your choice (1-4) if you want:
	'1. Singleplayer'
	'2. Multiplayer'
	'3. Instructions'
	'4. Exit'
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

