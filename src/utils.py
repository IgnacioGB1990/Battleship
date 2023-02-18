
import numpy as np
import constants as k
import random


def position_boat(eslora,tablero):
    while True:

        # 'N' - 'S' - 'E' - 'O'
        orient = random.choice(['N', 'S', 'E', 'O'])

        # Posicion inicial del barco
        current_pos = np.random.randint(10, size = 2)
    
        fila = current_pos[0]
        col = current_pos[1]
        
        # Recogemos las 4 posiciones colindantes a current_pos
        coors_posiN = tablero[fila:fila - eslora:-1, col]
        coors_posiE = tablero[fila, col: col + eslora]
        coors_posiS = tablero[fila:fila + eslora, col]
        coors_posiO = tablero[fila, col: col - eslora:-1]
        
        # Comprobamos si esas posiciones son validas
        # Orientacion Norte
        if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
            tablero[fila:fila - eslora:-1, col] = 'O'
            break

        # Orientacion Este
        elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
            tablero[fila, col: col + eslora] = 'O'
            break

        # Orientacion Sur
        elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
            tablero[fila:fila + eslora, col] = 'O'
            break

        # Orientacion Oeste
        elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
            tablero[fila, col: col - eslora:-1] = 'O'
            break

        # No cumple con las dimensiones del tablero, o hay un barco ahi
        # Probamos con otra coordenada
        else:
            continue


def seek_and_destroy(x,y,computerBoard,tablero_blanco_computer):
    if computerBoard[x,y]=="O":
        print(">>>>>>>>>>>>>>>  HIT <<<<<<<<<<<<<<< ")
        computerBoard[x,y]="X"
        tablero_blanco_computer[x,y]="X"
        k.boats_alive_computer-=1
    elif computerBoard[x,y]=="X" or computerBoard[x,y]=="-":
        print("You already tried to shoot that target!")
    else:
        computerBoard[x,y]="-"
        tablero_blanco_computer[x,y]="-"
        print("<<<<<<<<<<<<<<   WATER >>>>>>>>>>>>>>>")


def computerAttacks(playerBoard,x,y):

    if playerBoard[x,y]=="O":
        playerBoard[x,y]=="X"
        k.playerLives-=1
    
    
        
def generateRandomBoard(tablero):


    for eslora in k.boat_size_array:
        position_boat(eslora,tablero)
        #utils.position_boat(eslora,tablero_computer)
    

       
    



