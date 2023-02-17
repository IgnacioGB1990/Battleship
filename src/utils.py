
import numpy as np
import constants
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


def seek_and_destroy(x,y,tablero_computer):
    if tablero_computer[x,y]=="O":
        print("Boat hit! Go again: ")
        tablero_computer[x,y]="X"
        constants.boats_alive-=1
        print(tablero_computer)
    elif tablero_computer[x,y]=="X" or tablero_computer[x,y]=="-":
        print("Melón! Ya habías dado estas coordenadas")
    else:
        tablero_computer[x,y]="-"
        print("AGUA!")
        print(tablero_computer)

    
        

    

       
    



