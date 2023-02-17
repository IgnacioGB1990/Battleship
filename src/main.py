import numpy as np
import utils

# Barcos
# 4 boats with length of 1
# 3 boats with length of 2
# 2 boats with length of 3
# 1 boat with length of 4

tablero = np.full(fill_value = ' ', shape = (10, 10))
tablero_computer = np.full(fill_value = ' ', shape = (10, 10))

boat_size_array = [4,3,3,2,2,2,1,1,1,1]


for eslora in boat_size_array:
    utils.position_boat(eslora,tablero)
    utils.position_boat(eslora,tablero_computer)




print()    
print("Tu tablero")
print() 
print(tablero)
print()
print("El del ordenador")
print()
print(tablero_computer)

print("W E L C O M E !")
print("Empiezas tu a atacar:")
x = int(input("Introduce tu coordenada x: "))
y = int(input("Introduce tu coordenada y: "))

utils.seek_and_destroy(x,y,tablero_computer)
