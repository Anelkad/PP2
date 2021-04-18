import pygame
import random
import pickle
import time
import os

pygame.init()

score = 0
level = 1
#pickle_out = open("f.pickle","rb")
#ex = pickle.load(pickle_out)
#score = ex["score"]
#level = ex["level"]

clock = pygame.time.Clock()
sc_width = 600
sc_height = 400
sc = pygame.display.set_mode((sc_width,sc_height))

pygame.display.set_caption("Snake game")

gameover = False
font = pygame.font.SysFont('ComicSans', 30)

class Circle():
    def __init__(self, x = 0, y = 0):
        self.r = 5
        self.x = x
        self.y = y
        self.speed = 10
        self.hitbox = pygame.Rect(self.x-self.r,self.y-self.r,self.r*2,self.r*2)

    def draw(self):
        pygame.draw.circle(sc,(100,100,100),(self.x,self.y),self.r)

class Wall():
    def __init__(self,x ,y ):
        self.x = x
        self.y = y
        self.size = 20
        self.hitbox = pygame.Rect(self.x,self.y,self.size,self.size)
    
    def draw(self):
        self.hitbox = pygame.Rect(self.x,self.y,self.size,self.size)
        pygame.draw.rect(sc,(self.x%160,self.y%80,223),self.hitbox)

tail = []
walls = []

def create_map(level):
    with open(f'maps/map_{level}.txt', mode='r') as file:
        row_num = 0 
        for row in file:
            for block_num in range(len(row)):
                if row[block_num] == '1':
                    walls.append(Wall(block_num*20, row_num*20))
            row_num += 1

class Snakehead():
    def __init__(self):
        self.r = 5
        self.x = 15
        self.y = 15
        self.speed = 10
        self.dx = self.speed
        self.dy = 0
        self.hitbox = pygame.Rect(self.x-self.r,self.y-self.r,self.r*2,self.r*2)

    def draw(self):
        pygame.draw.circle(sc,(100,100,100),(self.x,self.y),self.r)

    def move(self):
        if len(tail)>0:
            for i in range(len(tail)-1):
                tail[i]=Circle(tail[i+1].x,tail[i+1].y)
            tail[len(tail)-1]=Circle(self.x,self.y)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx = -self.speed
                self.dy = 0
            if event.key == pygame.K_RIGHT:
                self.dx = self.speed
                self.dy = 0
            if event.key == pygame.K_UP:
                self.dx = 0
                self.dy = -self.speed
            if event.key == pygame.K_DOWN:
                self.dx = 0
                self.dy = self.speed
        self.y+=self.dy
        self.x+=self.dx
        self.hitbox = pygame.Rect(self.x-self.r,self.y-self.r,self.r*2,self.r*2)
        

head = Snakehead()

class Fruit():
    def __init__(self):
        self.r = 5
        self.x = random.randrange(5,sc_width-5,10)
        self.y = random.randrange(5,sc_height-5,10)
        self.hitbox = pygame.Rect(self.x-self.r,self.y-self.r,self.r*2,self.r*2)

    def draw(self):
        pygame.draw.circle(sc,(200,10,10),(self.x,self.y),self.r)

f = Fruit()

while not gameover:
    sc.fill((0,0,0))
    create_map(level)
    sc.blit(font.render("score "+str(score), 1, (255, 255, 255)), (sc_width*3//4,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            
    head.move()
    if head.y-5<0 or head.y+5>sc_height or head.x-5<0 or head.x+5>sc_width:
        gameover=True
    head.draw()

    for w in walls:
        w.draw()
        if head.hitbox.colliderect(w.hitbox):
            gameover = True
        if f.hitbox.colliderect(w.hitbox):
            f = Fruit()
    for c in tail:
        c.draw()
        if head.hitbox.colliderect(c.hitbox):
            gameover = True
    
    f.draw()
    if head.hitbox.colliderect(f.hitbox):
        score+=1
        f = Fruit()
        tail.append(Circle(head.x,head.y))

    if score//5 ==level:
        level+=1
        walls = []
        tail = []
        s = pygame.Surface((sc_width,sc_height))
        s.set_alpha(128)
        s.fill((0,0,200))
        sc.blit(s, (0,0))
        sc.blit(font.render("LEVEL "+str(level), 1, (255, 255, 255)), (sc_width/2-40,sc_height/2))
        pygame.display.update()
        time.sleep(2)
    
    clock.tick(10)
    pygame.display.update()

if gameover:
    s = pygame.Surface((sc_width,sc_height))
    s.set_alpha(128)
    s.fill((200,0,0))
    sc.blit(s, (0,0))
    sc.blit(font.render("Game Over", True, (255,0,0)), (sc_width//4,sc_height/2-70))
    sc.blit(font.render("Score : "+str(score), 1, (255, 255, 255)), (sc_width/2-30,sc_height/2))
    pygame.display.update()
    time.sleep(3)

dic = {
    "score" : score,
    "level" : level
}
pickle_out = open("f.pickle","wb")
pickle.dump(dic,pickle_out)
pickle_out.close()
