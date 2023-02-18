import numpy as np
import utils
import constants as k

playerBoard = np.full(fill_value = ' ', shape = (10, 10))
tablero_blanco = np.full(fill_value = ' ', shape = (10, 10))

tablero_blanco_computer = np.full(fill_value = ' ', shape = (10, 10))
computerBoard = np.full(fill_value = ' ', shape = (10, 10))
computerBoard[0:2,0:2]="O"



def playerMove():

    while k.computerLives>0:

        print("---------------  SHOTS FIRED -----------")
        print(tablero_blanco_computer)

        print("--------------   MY BOARD ------------")
        print(playerBoard)



        x = input("x: ")
        if x.lower()=="exit" or x.lower()=="surrender":
            print("GAME ENDED")
            break
        y = input("y: ")
        if y.lower()=="exit" or y.lower()=="surrender":
            print("GAME ENDED")
            break
        else:
            x = int(x)
            y = int(y)
            utils.seek_and_destroy(x,y,computerBoard,tablero_blanco_computer)
            print("Boats left:",k.computerLives)

def computerMove(playerBoard):

    while k.playerLives>0:

        attackCoord = np.random.randint(10, size = 2)

        x =  attackCoord[0]
        y = attackCoord[1]
        
        utils.computerAttacks(playerBoard,x,y)

# Hace falta 2 tableros que guarden los impactos efectuados. 

def main():

    print("Welcome to Battleship!")
    utils.generateRandomBoard(playerBoard)

    # aquí un while boats_alive_computer & boats_alive_player
    playerMove()
    
    if k.boats_alive_computer == 0:
        print("CONGRATULATIONS YOU WON !!!")

     



main()



