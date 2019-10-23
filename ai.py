import numpy as np

MAP_WIDTH = 25
MAP_HEIGHT = 25
body = np.zeros((MAP_WIDTH,  MAP_HEIGHT))

parts = {1:"Blood", 2:"Artery", 3:"Vein", 4:"Organ"}

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
        
start = (0,0)
end = (100,100)

organ_list = []

def free(x, y, length, width):
  for i in range(x, x+width):
    for j in range(y, y+length):
      if body[i][j] !=0:
        return 0
  return 1

def organs(n):
  for i in range(n):
    length = np.random.randint(2,10)
    width = np.random.randint(2,10)
    x = np.random.randint(0,MAP_WIDTH-length)
    y = np.random.randint(0,MAP_WIDTH-length)
    while(not free(x, y, length, width)):
      length = np.random.randint(2,10)
      width = np.random.randint(2,10)
      x = np.random.randint(0,MAP_WIDTH-length)
      y = np.random.randint(0,MAP_WIDTH-length)
    organ_list.append(Organ(x, y, width, length, i))

organs(7)

entry_points = []
for i in range()
    
    