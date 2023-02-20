import numpy as np
import utils
import time
import pygame
from pygame import mixer
import constants as k

playerBoard = np.full(fill_value = ' ', shape = (10, 10))

computerEmptyBoard = np.full(fill_value = ' ', shape = (10, 10))
computerBoard = np.full(fill_value = ' ', shape = (10, 10))

# COMMENT FOR FULL MATCH
computerBoard[0:2,0:2]="O" 

mixer.init()

def playerMove():

    while k.playerTurn:
        print("\n  ----- SHOTS FIRED:",k.playerShotsFired, "----- SHIPS LEFT",k.computerLives,"\n")
        print(computerEmptyBoard)

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
            utils.playerAttacks(x,y,computerBoard,computerEmptyBoard)

def computerMove(playerBoard):
    utils.computerAttacks(playerBoard)

        

def main():


    print("""

 ██████   █████  ███    ███ ███████     ███████ ████████  █████  ██████  ████████ 
██       ██   ██ ████  ████ ██          ██         ██    ██   ██ ██   ██    ██    
██   ███ ███████ ██ ████ ██ █████       ███████    ██    ███████ ██████     ██    
██    ██ ██   ██ ██  ██  ██ ██               ██    ██    ██   ██ ██   ██    ██    
 ██████  ██   ██ ██      ██ ███████     ███████    ██    ██   ██ ██   ██    ██    
                                                                                  
                                                                                  
 """)
    
    print("\nFor a more immersive experience don't forget to turn your sound ON\n")

    k.sounds("start")

    utils.generateRandomBoard(playerBoard)
    # UNCOMMENT FOR FULL MATCH
    # utils.generateRandomBoardComputer(computerBoard) 

    # print("\nThis is the computer board\n")
    # print(computerBoard)

    while (k.playerLives>0 or k.computerLives>0) and k.exitGame:

        if k.playerTurn and k.computerLives == 0:
            k.sounds("won")
            print("""

██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██     ██     ██     ██ 
 ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██     ██     ██     ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██     ██     ██     ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██                      
   ██     ██████   ██████       ███ ███   ██████  ██   ████     ██     ██     ██ 
                                                                                 
                                                                                 

            """)            
            time.sleep(3)
            break

        elif k.computerTurn and k.playerLives==0:
            k.sounds("lose")
            print("""

██    ██  ██████  ██    ██     ██       ██████  ███████ ███████ 
 ██  ██  ██    ██ ██    ██     ██      ██    ██ ██      ██      
  ████   ██    ██ ██    ██     ██      ██    ██ ███████ █████   
   ██    ██    ██ ██    ██     ██      ██    ██      ██ ██      
   ██     ██████   ██████      ███████  ██████  ███████ ███████ 
                                                                                                                       

            """)



            print("\n YOU LOSE !!!\n")
        
        elif k.playerTurn:
            playerMove()
        
        elif k.computerTurn:
            computerMove(playerBoard)     

main()



