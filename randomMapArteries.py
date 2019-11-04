# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:57:23 2019

@author: Varun
"""

import pygame as pg
import sys
from settings import *
from sprites import *
import numpy as np
#from snake import *


# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255,192,203)
BLUE = (127,255,212)
ORCHID = (153,50,204)

# game settings
WIDTH = 1000   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 1000  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 10
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#matrix = np.random.randint(0,4,(int(GRIDWIDTH),int(GRIDHEIGHT)))

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx,dy) and self.allowed_direction(dx,dy) :
            self.x += dx
            self.y += dy
        
    
    def collide_with_walls(self,dx=0,dy=0):
        for wall in self.game.walls:
            if wall.x == self.x+dx and wall.y == self.y+dy:
                return True
        return False    
   
    def allowed_direction(self,dx=0,dy=0):
        print(body[self.y][self.x].directions)
        if dx>0:
            if 'r' in body[self.y][self.x].directions :
                return True
        if dx<0:
            if 'l' in body[self.y][self.x].directions :
                return True
        if dy>0:
            if 'd' in body[self.y][self.x].directions :
                return True
        if dy<0:
            if 'u' in body[self.y][self.x].directions :
                return True
        return False    
        
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
     def __init__(self, game, x, y):
         self.groups = game.all_sprites, game.walls
         pg.sprite.Sprite.__init__(self, self.groups)
         self.game = game
         self.image = pg.Surface((TILESIZE, TILESIZE))
         self.image.fill(LIGHTGREY)
         self.rect = self.image.get_rect()
         self.x = x
         self.y = y
         self.rect.x = x * TILESIZE
         self.rect.y = y * TILESIZE

        
class Organ(pg.sprite.Sprite):
    def __init__(self,game,x,y,val):
        if val == 1:
            self.groups = game.all_sprites
            pg.sprite.Sprite.__init__(self,self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE    
        elif val == 2:
            self.groups = game.all_sprites
            pg.sprite.Sprite.__init__(self,self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(ORCHID)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE    
        elif val == 3:
            self.groups = game.all_sprites
            pg.sprite.Sprite.__init__(self,self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(PINK)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE    
        elif val == 4:
            self.groups = game.all_sprites
            pg.sprite.Sprite.__init__(self,self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(DARKGREY)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE   

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 50)
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        
        for row in range(np.size(b,0)):
            for col in range(np.size(b,1)):
                if body[row][col].t==0:
                    Wall(self,row,col)
                else:
                    Organ(self,row,col,b[row,col])
        
        
        xe,ye = entry_points[np.random.choice(len(entry_points))]
        self.player = Player(self, xe, ye)        
        
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()