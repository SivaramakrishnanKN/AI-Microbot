import numpy as np


'''
This function determines the speed of the bot through the given artery/vein
'''
def speed(width):
  return 1/width  

class Vessel:
  def __init__(self, x, y, width, length):
    self.width = width
    self.length = length
    self.x = x
    self.y = y
    
class Artery(Vessel):
  def __init__(self, x, y, width, length, thickness, direction):
    Vessel.__init__(x, y, width, length)
    self.direction = direction
    self.thickness = thickness
    
class Vein(Vessel):
  def __init__(self, x, y, width, length, thickness, direction):
    Vessel.__init__(x, y, width, length)
    self.direction = direction
    self.thickness = thickness
  
class Organ(Vessel):
  def __init__(self, x, y, width, length, index):    
    Vessel.__init__(self, x, y, width, length)
    self.index = index
    for i in range(x, x+width):
      for j in range(y, y+length):
        body[i][j] = 4

def free(x, y, length, width):
  for i in range(x, x+width):
    for j in range(y, y+length):
      if body[i][j] !=0:
        return 0
  return 1

def create_organs(n):
  for i in range(n):
    length = np.random.randint(2,10)
    width = np.random.randint(2,10)
    x = np.random.randint(0,MAP_WIDTH-width)
    y = np.random.randint(0,MAP_WIDTH-length)
    while(not free(x, y, length, width)):
      length = np.random.randint(2,10)
      width = np.random.randint(2,10)
      x = np.random.randint(0,MAP_WIDTH-width)
      y = np.random.randint(0,MAP_WIDTH-length)
    organ_list.append(Organ(x, y, width, length, i))

def valid(x, y):
    if x<0 or x>=MAP_WIDTH or y<0 or y>=MAP_HEIGHT:
        return 0
    return 1

def contact(x, y, part):
    if valid(x,y) and body[x][y]==part:
        return 1
    elif valid(x+1, y) and body[x+1][y]==part:
        return 1
    elif valid(x, y+1) and body[x][y+1]==part:
        return 1
    elif valid(x+1, y+1) and body[x+1][y+1]==part:
        return 1
    elif valid(x-1, y) and body[x-1][y]==part:
        return 1
    elif valid(x-1, y-1) and body[x-1][y-1]==part:
        return 1
    elif valid(x+1, y-1) and body[x+1][y-1]==part:
        return 1
    elif valid(x, y-1) and body[x][y-1]==part:
        return 1
    elif valid(x-1, y+1) and body[x-1][y+1]==part:
        return 1
    return 0

def create_entry(n):
    for i in range(n):
        x = np.random.randint(0,MAP_WIDTH)
        y = np.random.randint(0,MAP_HEIGHT)
        while contact(x,y,4):
            x = np.random.randint(0,MAP_WIDTH)
            y = np.random.randint(0,MAP_HEIGHT)
        entry_points.append((x,y))

def create_path(x_entry, y_entry, x_goal, y_goal):
    np.random.choice([2,3], p=[0.5, 0.5])
    
MAP_WIDTH = 25
MAP_HEIGHT = 25
body = np.zeros((MAP_WIDTH,  MAP_HEIGHT))
parts = {1:"Blood", 2:"Artery", 3:"Vein", 4:"Organ"}
organ_list = []
entry_points = []

create_organs(7)
create_entry(50)

  