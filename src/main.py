import numpy as np
import utils
import time
import pygame
from pygame import mixer
import constants as k

playerBoard = np.full(fill_value = ' ', shape = (10, 10))
tablero_blanco = np.full(fill_value = ' ', shape = (10, 10))

tablero_blanco_computer = np.full(fill_value = ' ', shape = (10, 10))
computerBoard = np.full(fill_value = ' ', shape = (10, 10))
computerBoard[0:2,0:2]="O"

mixer.init()

def playerMove():

    # while k.computerLives>0:
    while k.playerTurn:
        print("\n  ----- SHOTS FIRED:",k.playerShotsFired, "----- SHIP LEFT",k.computerLives,"\n")
        print(tablero_blanco_computer)

        print(" \n --------------- MY SHIPS --------------\n")
        print(playerBoard)

        if k.computerLives==0:
            break

        x = input("x: ")
        if x.lower()=="exit" or x.lower()=="quit":
            k.exitGame = False
            break
        y = input("y: ")
        if y.lower()=="exit" or y.lower()=="quit":
            k.exitGame = False
            break
        else:
            x = int(x)
            y = int(y)
            utils.playerAttacks(x,y,computerBoard,tablero_blanco_computer)

def computerMove(playerBoard):
    utils.computerAttacks(playerBoard)


         
        



def main():

    print("\n WELCOME TO BATTLESHIP ! \n")
    k.sounds("start")

    utils.generateRandomBoard(playerBoard)


    while (k.playerLives>0 or k.computerLives>0) and k.exitGame:

        if k.playerTurn and k.computerLives == 0:
            k.sounds("won")
            print("\nCONGRATULATIONS YOU WON !!!\n")            
            time.sleep(3)
            break

        elif k.computerTurn and k.playerLives==0:
            k.sounds("lose")
            print("\n YOU LOSE !!!\n")
        
        elif k.playerTurn:
            playerMove()
        
        elif k.computerTurn:
            computerMove(playerBoard)
    



    if k.playerLives ==0:
        print("YOU LOST")





     

main()



