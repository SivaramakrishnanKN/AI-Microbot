import numpy as np
import math

def distance(x,y, xg, yg):
    return abs(x-xg)+abs(y-yg)


def cost(x,y,xg,yg):
    cost=0
    cost+=(4-len(body[x][y].directions))
    cost+=body[x][y].thickness
    if body[x][y].t=='A':
        cost-=5
        print('A')
    cost+=0.5*distance(x,y,xg,yg)
    return cost

c = np.zeros((MAP_WIDTH,  MAP_HEIGHT))

xg,yg = organ_list[goal_organ].centroid


for x in range(MAP_WIDTH):
    for y in range(MAP_HEIGHT):
        c[x][y]=cost(x,y,xg,yg)        

def look_ahead(x,y,count):
    if count==1:
        c=[]
        for d in body[x][y].directions:
            if d=='d':
                c.append(cost(x+1,y,xg,yg))
            elif d=='u':
                c.append(cost(x-1,y,xg,yg))
            elif d=='l':
                c.append(cost(x,y-1,xg,yg))
            elif d=='r':
                c.append(cost(x,y+1,xg,yg))
        return min(c)
    c=[]
    for d in body[x][y].directions:
        if d=='d':
            c.append(cost(x+1,y,xg,yg)+look_ahead(x-1,y,count-1))
        elif d=='u':
            c.append(cost(x-1,y,xg,yg)+look_ahead(x-1,y,count-1))
        elif d=='l':
            c.append(cost(x,y-1,xg,yg)+look_ahead(x-1,y,count-1))
        elif d=='r':
            c.append(cost(x,y+1,xg,yg)+look_ahead(x-1,y,count-1))
    return min(c)

def get_direction(x,y):
    c=[]
    for d in body[x][y].directions:
        if d=='d':
            c.append(cost(x+1,y,xg,yg)+look_ahead(x-1,y,count-1),'d')
        elif d=='u':
            c.append(cost(x-1,y,xg,yg)+look_ahead(x-1,y,count-1),'u')
        elif d=='l':
            c.append(cost(x,y-1,xg,yg)+look_ahead(x-1,y,count-1),'l')
        elif d=='r':
            c.append(cost(x,y+1,xg,yg)+look_ahead(x-1,y,count-1),'r')
    key = min(cost)