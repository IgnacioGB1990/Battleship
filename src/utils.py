
import numpy as np
import pygame
from pygame import mixer
import constants as k
import random

mixer.init()

def position_boat(eslora,tablero):

    while True:

        orient = random.choice(['N', 'S', 'E', 'O'])

        current_pos = np.random.randint(10, size = 2)
    
        fila = current_pos[0]
        col = current_pos[1]
        
        coors_posiN = tablero[fila:fila - eslora:-1, col]
        coors_posiE = tablero[fila, col: col + eslora]
        coors_posiS = tablero[fila:fila + eslora, col]
        coors_posiO = tablero[fila, col: col - eslora:-1]
        
        if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
            tablero[fila:fila - eslora:-1, col] = 'O'
            break
        elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
            tablero[fila, col: col + eslora] = 'O'
            break
        elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
            tablero[fila:fila + eslora, col] = 'O'
            break
        elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
            tablero[fila, col: col - eslora:-1] = 'O'
            break
        else:
            continue

def generateRandomBoard(tablero):

    for eslora in k.boat_size_array:
        position_boat(eslora,tablero)
        
def generateRandomBoardComputer(tablero):

    for eslora in k.boat_size_array:
        position_boat(eslora,tablero)

def playerAttacks(x,y,computerBoard,computerEmptyBoard):

    if computerBoard[x,y]=="O":
        print("\n>>>>>>>>>>>>>>>  HIT <<<<<<<<<<<<<<<\n")
        computerBoard[x,y]=k.hit
        computerEmptyBoard[x,y]=k.hit
        k.playerShotsFired+=1
        k.computerLives-=1
        k.sounds("hit")

    elif computerBoard[x,y]==k.hit or computerBoard[x,y]==k.miss:
        k.sounds("error")
        print("\n You already tried to shoot that target! \n")
    else:
        computerBoard[x,y]=k.miss
        computerEmptyBoard[x,y]=k.miss
        k.playerShotsFired+=1
        k.playerTurn = False
        k.computerTurn = True
        k.sounds("splash")
        print("\n<<<<<<<<<<<<<<   WATER >>>>>>>>>>>>>>>\n")

def computerAttacks(playerBoard):

    attackCoord = np.random.randint(10, size = 2)
    x =  attackCoord[0]
    y = attackCoord[1]

    if playerBoard[x,y]=="O":
        playerBoard[x,y]=k.hit
        k.playerLives-=1
        print("\n COMPUTER HITS YOU :",x,y,"\n")
        print(playerBoard)
    
    elif playerBoard[x,y]==k.hit:
        print("\nComputer tried to hit target already hit, but tries again",x,y,"\n")

    elif playerBoard[x,y]==" ":
        playerBoard[x,y]=k.miss
        k.computerTurn = False
        k.playerTurn = True

        print("\n COMPUTER MISSED :",x,y,"\n")


        




    
    
        

    

       
    



