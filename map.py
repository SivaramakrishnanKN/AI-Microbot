import numpy as np

'''
This function determines the speed of the bot through the given artery/vein
'''
def speed(max_speed,width):
  return max_speed/width  

'''
This class determines what type of vessel is present in a particular coordinate in the body
'''    
class Vessel():
    def __init__(self, thickness, directions, t):
        self.t = t
        self.directions = directions
        self.thickness = thickness
    
'''
This class contains information about each Organ
'''
class Organ():
  def __init__(self, x, y, width, length, index):    
    self.index = index
    self.x=x
    self.y=y
    self.width=width
    self.length=length
    self.centroid=(x+width/2,y+length/2)
    for i in range(x, x+width):
      for j in range(y, y+length):
        body[i][j] = Vessel(index,['d','u','l','r'],4)

def free(x, y, length, width):        
    for i in range(x, x+width):
        for j in range(y, y+length):
            if body[i][j].t !=0:
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
    if valid(x,y) and body[x][y].t==part:
        return 1,body[x][y].thickness
    elif valid(x+1, y) and body[x+1][y].t==part:
        return 1,body[x+1][y].thickness
    elif valid(x, y+1) and body[x][y+1].t==part:
        return 1,body[x][y+1].thickness
    elif valid(x+1, y+1) and body[x+1][y+1].t==part:
        return 1,body[x+1][y+1].thickness
    elif valid(x-1, y) and body[x-1][y].t==part:
        return 1,body[x-1][y].thickness
    elif valid(x-1, y-1) and body[x-1][y-1].t==part:
        return 1,body[x-1][y-1].thickness
    elif valid(x+1, y-1) and body[x+1][y-1].t==part:
        return 1,body[x+1][y-1].thickness
    elif valid(x, y-1) and body[x][y-1].t==part:
        return 1,body[x][y-1].thickness
    elif valid(x-1, y+1) and body[x-1][y+1].t==part:
        return 1,body[x-1][y+1].thickness
    return 0,0

def create_entry(n):
    for i in range(n):
        x = np.random.randint(0,MAP_WIDTH)
        y = np.random.randint(0,MAP_HEIGHT)
        while contact(x,y,4)!=(0,0):
            x = np.random.randint(0,MAP_WIDTH)
            y = np.random.randint(0,MAP_HEIGHT)
        entry_points.append((x,y))

#def get_direction(x, y, directions, c):
#    x1,y1=x,y
#    if c=='A':
#        c1='V'
#    elif c=='V':
#        c1='A'
#
#    direction = np.random.choice(directions)
#    directions.remove(direction)    
#    if direction=='u':
#        x1-=1
#    elif direction=='d':
#        x1+=1
#    elif direction=='l':
#        y1-=1
#    elif direction=='r':
#        y1+=1
#    if body[x1][y1].t!=c1 and valid(x1,y1):
#        return direction
#    else:
#        while body[x1][y1].t==c1 or not valid(x1,y1):
#            if len(directions)==0:
#                return -1
#            x1,y1=x,y
#            direction = np.random.choice(directions)
#            directions.remove(direction)    
#            if direction=='u':
#                x1-=1
#            elif direction=='d':
#                x1+=1
#            elif direction=='l':
#                y1-=1
#            elif direction=='r':
#                y1+=1
#                
#        return direction

def get_direction(x, y, directions,c,min_length,max_length):
#    x = 0
#    y = 0
#    c='A'
#    min_length=2
#    max_length=15
    if c=='A':
        c1='V'
    elif c=='V':
        c1='A'
        
    flag=0
    while not flag:
        if len(directions)==0:
            break
        direction = np.random.choice(directions)
        directions.remove(direction)    
        if direction=='u':
            lengths=list(range(min_length,max_length))
            while not flag:
                if len(lengths)==0:
                    break
                length = np.random.choice(lengths)
                lengths.remove(length)                
                for i in range(length):
                    if not valid(x-i,y) or body[x-i][y].t==c1:
                       flag=0
                       break
                    flag=1
            if flag==1:
                return direction,length

        elif direction=='d':
            lengths=list(range(min_length,max_length))
            while not flag:
                length = np.random.choice(lengths)
                lengths.remove(length)
                if len(lengths)==0:
                    break
                for i in range(length):
                    if not valid(x+i,y) or body[x+i][y].t==c1:
                       flag=0
                       break
                    flag=1
            if flag==1:
                return direction,length

        elif direction=='l':
            lengths=list(range(min_length,max_length))
            while not flag:
                length = np.random.choice(lengths)
                lengths.remove(length)
                if len(lengths)==0:
                    break
                for i in range(length):
                    if not valid(x,y-i) or body[x][y-i].t==c1:
                       flag=0
                       break
                    flag=1
            if flag==1:
                return direction,length

        elif direction=='r':
            lengths=list(range(min_length,max_length))
            while not flag:
                length = np.random.choice(lengths)
                lengths.remove(length)
                if len(lengths)==0:
                    break
                for i in range(length):
                    if not valid(x,y+i) or body[x][y+i].t==c1:
                       flag=0
                       break
                    flag=1
            if flag==1:
                return direction,length

    return -1,-1


def get_new_direction(x, y, directions, c):
    x1,y1=x,y
    if c=='A':
        c1='V'
    elif c=='V':
        c1='A'

    direction = np.random.choice(directions)
    directions.remove(direction)    
    if direction=='u':
        x1-=1
    elif direction=='d':
        x1+=1
    elif direction=='l':
        y1-=1
    elif direction=='r':
        y1+=1
    if valid(x1,y1) and body[x1][y1].t!=c1:
        return x1,y1
    else:
        while not valid(x1,y1) or body[x1][y1].t==c1:
            if len(directions)==0:
                return -1,-1
            x1,y1=x,y
            direction = np.random.choice(directions)
            directions.remove(direction)    
            if direction=='u':
                x1-=1
            elif direction=='d':
                x1+=1
            elif direction=='l':
                y1-=1
            elif direction=='r':
                y1+=1
         
        return x1,y1


def create_path(x_entry, y_entry, thick, c, inc,cnt):
    flag=0
#    length = 0
#    d = 0
#    x_entry = 0
#    y_entry = 0
#    c = 'A'
#    thick = 4
    if c=='A':
        c1='V'
    elif c=='V':
        c1='A'


    while not flag:
        length = np.random.randint(2,15)
        directions = ['u','d','l','r']
        d,length = get_direction(x_entry, y_entry, directions, c, 2,15)
        if d==-1:
            print("Not possible",x_entry,y_entry,c, thick)
            return
        if d=='u':
            for i in range(length):
                if body[x_entry-i][y_entry].t==c1 or not valid(x_entry-i,y_entry):
                    flag=0
                    break
                flag=1
        elif d=='d':
            for i in range(length):
                if body[x_entry+i][y_entry].t==c1 or not valid(x_entry+i,y_entry):
                    flag=0
                    break
                flag=1
        elif d=='l':
            for i in range(length):
                if body[x_entry][y_entry-i].t==c1 or not valid(x_entry,y_entry-i):
                    flag=0
                    break
                flag=1
        elif d=='r':
            for i in range(length):
                if body[x_entry][y_entry+i].t==c1 or not valid(x_entry,y_entry+i):
                    flag=0
                    break
                flag=1
    print(length,d,c,thick)                
    
    for i in range(length):
        if d=='u':
            if body[x_entry-i][y_entry].t==4:
                print(x_entry-i,y_entry)
                return
            if body[x_entry-i][y_entry].t==0:
                if c=='V':
                    body[x_entry-i][y_entry] = Vessel(thick, set(['u']),c)    
                    print(1)
                else:
                    body[x_entry-i][y_entry] = Vessel(thick, set(['u','d']),c)
                    print(2)
            else:
                if c=='V':
                    body[x_entry-i][y_entry].directions.add('u')
                    print(3)
                else:
                    body[x_entry-i][y_entry].directions.add('u')
                    body[x_entry-i][y_entry].directions.add('d')
                    print(4)
                body[x_entry-i][y_entry].thickness=max(body[x_entry-i][y_entry].thickness,thick)

        elif d=='d':
            if body[x_entry+i][y_entry].t==4:
                print(x_entry+i,y_entry)
                return
            if body[x_entry+i][y_entry].t==0:
                if c=='V':
                    body[x_entry+i][y_entry] = Vessel(thick, set(['d']),c)    
                    print(1)
                else:
                    body[x_entry+i][y_entry] = Vessel(thick, set(['u','d']),c)
                    print(2)
            else:
                if c=='V':
                    body[x_entry+i][y_entry].directions.add('d')
                    print(3)
                else:
                    body[x_entry+i][y_entry].directions.add('d')
                    body[x_entry+i][y_entry].directions.add('u')
                    print(4)
                body[x_entry+i][y_entry].thickness=max(body[x_entry+i][y_entry].thickness,thick)
        
        elif d=='l':
            if body[x_entry][y_entry-i].t==4:
                print(x_entry,y_entry-i)
                return
            if body[x_entry][y_entry-i].t==0:
                if c=='V':
                    print(1)
                    body[x_entry][y_entry-i] = Vessel(thick, set(['l']),c)    
                else:
                    body[x_entry][y_entry-i] = Vessel(thick, set(['l','r']),c)
                    print(2)
            else:
                if c=='V':
                    body[x_entry][y_entry-i].directions.add('l')
                    print(3)
                else:
                    body[x_entry][y_entry-i].directions.add('l')
                    body[x_entry][y_entry-i].directions.add('r')
                    print(4)
                body[x_entry][y_entry-i].thickness=max(body[x_entry][y_entry-i].thickness,thick)

        elif d=='r':
            if body[x_entry][y_entry+i].t==4:
                print(x_entry,y_entry+i)
                return
            if body[x_entry][y_entry+i].t==0:
                if c=='V':
                    body[x_entry][y_entry+i] = Vessel(thick, set(['r']),c)    
                    print(1)
                else:
                    body[x_entry][y_entry+i] = Vessel(thick, set(['r','l']),c)
                    print(2)
            else:
                if c=='V':
                    body[x_entry][y_entry+i].directions.add('r')
                    print(3)
                else:
                    body[x_entry][y_entry+i].directions.add('r')
                    body[x_entry][y_entry+i].directions.add('l')
                    print(4)
                body[x_entry][y_entry+i].thickness=max(body[x_entry][y_entry+i].thickness,thick)

    print("Appended")
    length-=1    
    # Generating new thickness
    if inc:
        new_thick = np.random.randint(thick,11)
    else:
        new_thick = np.random.randint(1,thick+1)
    # Recursively generating new path from the end point
    if d=='u':
        if new_thick<2:
            # Case to swap Artery and Vein
            if cnt==3:
                return
            if c == 'A':
                directions = ['u','d','l','r']
                x1,y1=get_new_direction(x_entry-length,y_entry,directions,'V')
                if x1==-1:
                    print("Snake")
                    return 
                create_path(x1,y1,new_thick,'V', not inc,cnt+1)
            else:
                directions = ['u','d','l','r']
                x1,y1=get_new_direction(x_entry-length,y_entry,directions,'A')
                if x1==-1:
                    print("Snake")
                    return 
                create_path(x1,y1,new_thick,'A', not inc,cnt+1)
        else:
            if new_thick==10:
                create_path(x_entry-length,y_entry,new_thick,c,not inc,cnt)
            else:
                create_path(x_entry-length,y_entry,new_thick,c,inc,cnt)
            
    elif d=='d':
        if new_thick<2:
            if cnt==3:
                return
            if c == 'A':
                directions = ['u','d','l','r']
                x1,y1=get_new_direction(x_entry+length,y_entry,directions,'V')
                if x1==-1:
                    print("Snake")
                    return 
                create_path(x1,y1,new_thick,'V', not inc,cnt+1)
            else:
                directions = ['u','d','l','r']
                x1,y1=get_new_direction(x_entry-length,y_entry,directions,'A')
                if x1==-1:
                    print("Snake")
                    return 
                create_path(x1,y1,new_thick,'A', not inc,cnt+1)
        else:
            if new_thick==10:
                create_path(x_entry+length,y_entry,new_thick,c,not inc,cnt)
            else:
                create_path(x_entry+length,y_entry,new_thick,c,inc,cnt)
            
    elif d=='l':
        if new_thick<2:
            if cnt==3:
                return
            if c == 'A':
                directions = ['u','d','l','r']
                x1,y1=get_new_direction(x_entry,y_entry-length,directions,'V')
                if x1==-1:
                    print("Snake")
                    return 
                create_path(x1,y1,new_thick,'V', not inc,cnt+1)
            else:
                directions = ['u','d','l','r']
                x1,y1=get_new_direction(x_entry,y_entry-length,directions,'A')
                if x1==-1:
                    print("Snake")
                    return 
                create_path(x1,y1,new_thick,'A', not inc,cnt+1)
        else:
            if new_thick==10:
                create_path(x_entry,y_entry-length,new_thick,c,not inc,cnt)
            else:
                create_path(x_entry,y_entry-length,new_thick,c,inc,cnt)
            
    elif d=='r':
        if new_thick<2:
            if cnt==3:
                return
            if c == 'A':
                directions = ['u','d','l','r']
                x1,y1=get_new_direction(x_entry,y_entry+length,directions,'V')
                if x1==-1:
                    print("Snake")
                    return 
                create_path(x1,y1,new_thick,'V', not inc,cnt+1)
            else:
                directions = ['u','d','l','r']
                x1,y1=get_new_direction(x_entry,y_entry+length,directions,'A')
                if x1==-1:
                    print("Snake")
                    return 
                create_path(x1,y1,new_thick,'A', not inc,cnt+1)
        else:
            if new_thick==10:
                create_path(x_entry,y_entry+length,new_thick,c,not inc,cnt)
            else:
                create_path(x_entry,y_entry+length,new_thick,c,inc,cnt)


MAP_WIDTH = 100
MAP_HEIGHT = 100
b = np.zeros((MAP_WIDTH,  MAP_HEIGHT))
body = np.full((MAP_WIDTH,  MAP_HEIGHT), Vessel(0,[],0), dtype=object)
body[86][7].t
parts = {1:"Wall", 2:"Artery", 3:"Vein", 4:"Organ"}
organ_list = []
entry_points = []

create_organs(7)
create_entry(30)

for x,y in entry_points:
    create_path(x,y,10,'V',0,-25)

for i in range(MAP_WIDTH):
    for j in range(MAP_HEIGHT):
        if body[i][j].t=='A':
            b[i][j] = 2
        elif body[i][j].t=='V':
            b[i][j] = 3
        else:
            b[i][j]=body[i][j].t

#np.save("body.npy",body)
x,y = entry_points[np.random.choice(len(entry_points))]
print(body[x][y].directions)