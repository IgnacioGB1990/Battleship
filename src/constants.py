# Barcos
# 4 boats with length of 1
# 3 boats with length of 2
# 2 boats with length of 3
# 1 boat with length of 4

import numpy as np
import pygame
from pygame import mixer

mixer.init()


hit = "✅"
miss = "❌"


boat_size_array = [4,3,3,2,2,2,1,1,1,1]

computerLives = 4
playerLives = 20

playerTurn = True
computerTurn = False


playerShotsFired = 0
computerShotsFired = 0

exitGame = True

# hit = "X"
# miss = "-"


def sounds(sound):
  mixer.music.load("./src/assets/" +sound+".mp3")
  mixer.music.set_volume(0.4)
  mixer.music.play()

    
  
       

  

d = {
  "a":{
      "boats": 4,
      "length": 1
  },
    "b":{
      "boats": 3,
      "length": 2
  },
    "c":{
      "boats": 2,
      "length": 3
  },
    "d":{
      "boats": 1,
      "length": 4
  },

}