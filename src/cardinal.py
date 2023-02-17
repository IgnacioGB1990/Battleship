
import numpy as np
import constants


# N O R T H
# def check_north(start_x,slice_tablero,x,y):
#     if x<3:
#         print("Lo siento pero te sales del tablero!")
#     else:
#         check_boat_position_available_north(start_x,slice_tablero,x,y)

# def check_boat_position_available_north(start_x,slice,x,y): 
#     for boat in np.nditer(slice):
#         if boat == "O":
#             print("Ya existe un barco!")
#             break
#     else:
#         constants.tablero[ start_x:x, y:y+1 ]="O"
        
#         print("Coast is clear")  

# # S O U T H
# def check_boat_position_available_south(stop_x,slice,x,y): 
#     for boat in np.nditer(slice):
#         if boat == "O":
#             print("Ya existe un barco!")
#             break
#     else:
#         constants.tablero[ x:stop_x, y:y+1 ]="O"
#         print("Coast is clear")

            

# def check_south(stop_x,slice_tablero,x,y):
#     if stop_x>10:
#         print("Lo siento pero te sales del tablero!")
#     else:
#         check_boat_position_available_south(stop_x,slice_tablero,x,y)


# # E A S T   = = = = >
# def check_boat_position_available_east(stop_y,slice,x,y): 
#     for boat in np.nditer(slice):
#         if boat == "O":
#             print("Ya existe un barco!")
#             break
#     else:
#         constants.tablero[ x:x+1, y:stop_y ]="O"
#         print("Coast is clear")

# def check_east(stop_y,slice_tablero,x,y):
#     if stop_y>10:
#         print("Lo siento pero te sales del tablero!")
#     else:
#         check_boat_position_available_east(stop_y,slice_tablero,x,y)



# # W E S T    < = = = =
# def check_boat_position_available_west(start_y,slice,x,y): 
#     for boat in np.nditer(slice):
#         if boat == "O":
#             print("Ya existe un barco!")
#             break
#     else:
#         constants.tablero[ x:x+1, start_y+1:y+1 ]="O"
#         print("Coast is clear")

# def check_west(start_y,slice_tablero,x,y):
#     if start_y<-1:
#         print("Lo siento pero te sales del tablero!")
#     else:
#         check_boat_position_available_west(start_y,slice_tablero,x,y)