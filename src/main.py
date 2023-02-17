import numpy as np
import utils
import constants
# Barcos
# 4 boats with length of 1
# 3 boats with length of 2
# 2 boats with length of 3
# 1 boat with length of 4

tablero = np.full(fill_value = ' ', shape = (10, 10))
tablero_computer = np.full(fill_value = ' ', shape = (10, 10))

tablero_computer[0:2,0:2]="O"
boat_size_array = [4,3,3,2,2,2,1,1,1,1]




for eslora in boat_size_array:
    utils.position_boat(eslora,tablero)
    #utils.position_boat(eslora,tablero_computer)




  
print("Tu tablero")
print(tablero)
print("El del ordenador")
print(tablero_computer)


while constants.boats_alive>0:


    x = input("Introduce tu coordenada x: ")
    if x.lower()=="exit" or x.lower()=="surrender":
        print("GAME ENDED")
        break
    y = input("Introduce tu coordenada y: ")
    if y.lower()=="exit" or y.lower()=="surrender":
        print("GAME ENDED")
        break
    else:
        x = int(x)
        y = int(y)
        utils.seek_and_destroy(x,y,tablero_computer)
        print(constants.boats_alive)


if constants.boats_alive ==0:
    print("CONTRATULATIONS YOU WON !!!") 

    
    



