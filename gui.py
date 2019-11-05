import pygame as pg
import sys
from settings import *
from sprites import *
import numpy as np
from map import *
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
HOT_PINK = (255,105,180)
# game settings
WIDTH = 700   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 700  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "AI MicroBot"
BGCOLOR = DARKGREY

TILESIZE = 7
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

#matrix = np.random.randint(0,4,(int(GRIDWIDTH),int(GRIDHEIGHT)))

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREY)
        self.score=10000
        self.goal=0
#        self.image = pg.image.load(os.path.abspath("goku.gif"))
#        self.image = pg.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.next = next_direction(self.y,self.x,g.xg,g.yg)
    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx,dy): #and self.allowed_direction(dx,dy) :
            self.x += dx
            self.y += dy
            self.score-=cost(self.y,self.x,g.xg,g.yg)
            print(body[self.y][self.x].directions, self.x, self.y)
#            pg.key.set_repeat(body[self.y][self.x].thickness*25, 50)
            self.next = next_direction(self.y,self.x,g.xg,g.yg)
            if contact(self.y,self.x,4)!=(0,0):
                print("Goal")
                organ=organ_list[contact(self.y,self.x,4)[1]]
                for x in range(organ.x,organ.x+organ.width):
                    for y in range(organ.y,organ.y+organ.length):
                        if contact(self.y,self.x,4)[1]==g.goal_organ:
                            Organ(g,y,x,5)
                            self.goal=1
                        else:
                            Organ(g,y,x,6)
                            self.goal=-1
            else:
                self.goal=0
#                sys.exit()
#            flag=0
#            for d in body[self.y][self.x].directions:
#                print(d)
#                if d=='u':
#                    if body[self.y][self.x+1].t!=0:
#                        flag=1
#                if d=='d':
#                    if body[self.y][self.x-1].t!=0:
#                        flag=1
#                if d=='l':
#                    if body[self.y-1][self.x].t!=0:
#                        flag=1
#                if d=='r':
#                    if body[self.y+1][self.x].t!=0:
#                        flag=1
#            if flag==0:
#                print("Deadend")
#                sys.exit()
                
    def collide_with_walls(self,dx=0,dy=0):
        for wall in self.game.walls:
            if wall.x == self.x+dx and wall.y == self.y+dy:
                return True
        return False    
   
#    def allowed_direction(self,dx=0,dy=0):
#        print(body[self.x][self.y].directions, body[self.x][self.y].t, self.x, self.y)
#        if dx>0:
#            print('r')
#            if 'r' in body[self.y][self.x].directions :
#                return True
#        if dx<0:
#            print('l')
#            if 'l' in body[self.y][self.x].directions :
#                return True
#        if dy>0:
#            print('d')
#            if 'd' in body[self.y][self.x].directions :
#                return True
#        if dy<0:
#            print('u')
#            if 'u' in body[self.y][self.x].directions :
#                return True
#        return False    
        
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
            self.image.fill(RED)
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
            self.image.fill(BLUE)
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
            self.image.fill(PINK)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE   
        elif val == 5:
            self.groups = game.all_sprites
            pg.sprite.Sprite.__init__(self,self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(GREEN)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE   
        elif val == 6:
            self.groups = game.all_sprites
            pg.sprite.Sprite.__init__(self,self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(BLACK)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE   
        elif val == 7:
            self.groups = game.all_sprites
            pg.sprite.Sprite.__init__(self,self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(HOT_PINK)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE   

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH+200, HEIGHT))
        
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(100, 50)
        self.load_data()

    def load_data(self):
        pass

    def print_stat(self,t):
        font = pg.font.Font('freesansbold.ttf',15)
        text3 = font.render(t, True, WHITE)
        TextRect = text3.get_rect()
        TextRect.center = (WIDTH+(200/2),650)
        self.screen.blit(text3,TextRect)


    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        
        for row in range(np.size(b,0)):
            for col in range(np.size(b,1)):
                if body[row][col].t==0:
                    Wall(self,col,row)
                else:
                    Organ(self,col,row,b[row][col])
        
        ye,xe = entry_points[np.random.choice(len(entry_points))]
        print(xe,ye)
        
        self.goal_organ = np.random.choice(len(organ_list))
        organ = organ_list[self.goal_organ]
        for x in range(organ.x,organ.x+organ.width):
            for y in range(organ.y,organ.y+organ.length):
                Organ(g,y,x,7)
                
        self.xg,self.yg = organ_list[self.goal_organ].centroid

        self.player = Player(self, xe, ye)        
        
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            
#            pg.time.wait(10000)
#            self.automate()
#            
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
        scoreboard = pg.Surface((200,HEIGHT))
        scoreboard.fill(DARKGREY)        
        self.screen.blit(scoreboard,(WIDTH,0))
        
        font = pg.font.Font('Antonio-Regular.ttf',32)
        text = font.render("Scoreboard", True, WHITE)
        TextRect = text.get_rect()
        TextRect.center = (WIDTH+(200/2),40)
        self.screen.blit(text,TextRect)

        if self.player.goal==1:
            font = pg.font.Font('Antonio-Bold.ttf',35)
            text3 = font.render("SUCCESSFUL", True, GREEN)
            TextRect = text3.get_rect()
            TextRect.center = (WIDTH+(200/2),600)
            self.screen.blit(text3,TextRect)
        if self.player.goal==-1:
            self.player.score-=10
            font = pg.font.Font('Antonio-Bold.ttf',35)
            text3 = font.render("FAILED", True, RED)
            TextRect = text3.get_rect()
            TextRect.center = (WIDTH+(200/2),600)
            self.screen.blit(text3,TextRect)


        pg.draw.rect(self.screen,RED,(WIDTH+10,75,180,60))        
        pg.draw.rect(self.screen,BLACK,(WIDTH+15,80,170,50))        

#        board = pg.image.load('score.png')
#        board = pg.transform.scale(board, (190,80))
#        self.screen.blit(board, (WIDTH+5,75))
        
        font = pg.font.Font('digital-7.ttf',35)
        t=str(self.player.score)
        text1 = font.render(t, True, WHITE)
        TextRect = text1.get_rect()
        TextRect.center = (WIDTH+(200/2),100)
        self.screen.blit(text1,TextRect)
        
        
        font = pg.font.Font('freesansbold.ttf',15)
        t="Recommended Direction"
        text1 = font.render(t, True, WHITE)
        TextRect = text1.get_rect()
        TextRect.center = (WIDTH+(200/2),200)
        self.screen.blit(text1,TextRect)

        d = self.player.next
        if d=='d':
            board = pg.image.load('down.png')
            board = pg.transform.scale(board, (50,50))
            self.screen.blit(board, (WIDTH+75,300))
        elif d=='u':
            board = pg.image.load('up.png')
            board = pg.transform.scale(board, (50,50))
            self.screen.blit(board, (WIDTH+75,200))
        elif d=='l':
            board = pg.image.load('left.png')
            board = pg.transform.scale(board, (50,50))
            self.screen.blit(board, (WIDTH+25,250))
        elif d=='r':
            board = pg.image.load('right.png')
            board = pg.transform.scale(board, (50,50))
            self.screen.blit(board, (WIDTH+125,250))
        

        font = pg.font.Font('freesansbold.ttf',15)
        text1 = font.render("Moves Available", True, WHITE)
        TextRect = text1.get_rect()
        TextRect.center = (WIDTH+(200/2),400)
        self.screen.blit(text1,TextRect)
        
        for d in body[self.player.y][self.player.x].directions:
            if d=='d':
                board = pg.image.load('down.png')
                board = pg.transform.scale(board, (50,50))
                self.screen.blit(board, (WIDTH+75,500))
            elif d=='u':
                board = pg.image.load('up.png')
                board = pg.transform.scale(board, (50,50))
                self.screen.blit(board, (WIDTH+75,400))
            elif d=='l':
                board = pg.image.load('left.png')
                board = pg.transform.scale(board, (50,50))
                self.screen.blit(board, (WIDTH+25,450))
            elif d=='r':
                board = pg.image.load('right.png')
                board = pg.transform.scale(board, (50,50))
                self.screen.blit(board, (WIDTH+125,450))

#                font = pg.font.Font('freesansbold.ttf',16)
#                text = font.render(d, True, WHITE)
#                TextRect = text.get_rect()
#                TextRect.center = (WIDTH+(200/2),400+count*20)
#                self.screen.blit(text,TextRect)
#                count+=1
    
        font = pg.font.Font('freesansbold.ttf',15)
        text3 = font.render("Press R to reset game", True, WHITE)
        TextRect = text3.get_rect()
        TextRect.center = (WIDTH+(200/2),650)
        self.screen.blit(text3,TextRect)


        pg.display.flip()
        
    def automate(self):
        next_dir = self.next
        if next_dir == 'u':
            self.player.move(dy=-1)
        elif next_dir == 'd':
            self.player.move(dy=+1)
        elif next_dir == 'l':
            self.player.move(dx=-1)
        elif next_dir == 'r':    
            self.player.move(dx=+1)
        else:
            print("Not possible")
            pg.quit()
            sys.exit()
    def events(self):    
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    if 'l' in body[self.player.y][self.player.x].directions:
                        self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    if 'r' in body[self.player.y][self.player.x].directions:
                        self.player.move(dx=+1)
                if event.key == pg.K_UP:
                    if 'u' in body[self.player.y][self.player.x].directions:
                        self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    if 'd' in body[self.player.y][self.player.x].directions:
                        self.player.move(dy=+1)
                if event.key == pg.K_r:
                    self.new()
                    
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