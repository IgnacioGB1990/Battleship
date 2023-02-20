# Battleship ⛴
Battleship game developed using Python, Numpy and Pygame.

In this version of the game the user will be able to play against the computer a simplified version of Battleship.


# How to play

1. Each player will be assigned a random ship position prior the start of the game. 
The number of ships consist of :

* 4 ships with length of 1
* 3 ships with length of 2
* 2 ships with length of 3
* 1 ship with length of 4

2. For every successful hit the user gets another try.

3. Match ends when player/computer manages to sink all rivals ships.

4. Coordinates ( x, y ) will range between 0 and 9.

### Legend
1. ❌ = water
2. ✅ = part of ship damaged
3. "O" = ship position


> **Warning**

> For the purpose of the demo only 4 boats are assigned to the computer.
> Coordinates (0,0), (0,1), (1,0) and (1,1).

### For full match

Uncomment:

Line 68 in main.py

Line 25 in constants.py

Comment:

Line 14 in main.py

Line 28 in constants.py

### How to run

1. Copy on terminal:

```
git clone https://github.com/IgnacioGB1990/Battleship.git
```

2. Go to /src folder

3. Open main.py

4. On VS Code Run => Run => Run Without Debugging


> **Note**

> For a more immersive experience don't forget to turn your computer´s sound on 🎶