import pygame
import random
import time

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Game")

#screen
sc_height = 600
sc_width = 550
start = sc_width//5
screen = pygame.display.set_mode((sc_width,sc_height))
road_w = sc_width*2//3
road_h = sc_height
table = pygame.Surface((95,60))


font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, (255,0,0))

score = 0
score1 = 0
level = 1
case = 0
pygame.display.set_caption("Game")

class rrect():
    def __init__(self, y = 0, width=30 , height = 100, speed = 18):
        self.width = width
        self.height = height
        self.speed = speed
        self.y = y
        self.x = start +road_w//2 - self.width/2

    def draw(self):
        pygame.draw.rect(screen,(255,255,255),pygame.Rect(self.x,self.y,self.width,self.height))

    def fall(self):
        self.y+=self.speed
        if self.y > sc_height:
            self.y = -self.height - 50

class Enemy:
    def __init__(self,  width=40, height=80):
        self.width = width
        self.height = height
        self.x = random.randint(start,road_w + start - self.width)
        self.y = 0
        self.speed = random.randint(18+score1//5,40+score1//5*(case))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(pygame.transform.scale(
            pygame.image.load('Enemy.png'), (self.width, self.height)), (self.x, self.y))
        if self.hitbox.colliderect(car.hitbox):
            screen.blit(pygame.transform.scale(
                pygame.image.load('bang.png'), (self.width*2, self.height)), (self.x-self.width, self.y))

    def fall(self):
        global level
        global score
        self.y += self.speed
        if self.hitbox.colliderect(car.hitbox):
            pygame.mixer.music.load('crash.wav')
            pygame.mixer.music.play(1)
            time.sleep(1)
            score +=1
            self.y = - self.height
            self.x = random.randint(start,road_w + start - self.width)
            self.speed = random.randint(18+score1//5,40+score1//5*(case))
        elif self.y > sc_height + self.height:
            level +=1
            self.y = - self.height
            self.x = random.randint(start,road_w + start - self.width)
            self.speed = random.randint(18+score1//5,40+score1//5*(case))
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
       

class Car:
    def __init__(self,  width=40, height=80, speed=18):
        self.width = width
        self.height = height
        self.speed = speed
        self.x = start + road_w//2
        self.y = sc_height - self.height - 5
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(pygame.transform.scale(
            pygame.image.load('Player.png'), (self.width, self.height)), (self.x, self.y))
       

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            if self.x + self.width <= road_w + start:
                self.x+=self.speed
        if pressed_keys[pygame.K_LEFT]:
            if self.x - self.width/2 >= start:
                self.x-=self.speed
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

car = Car()
evilcar = Enemy()
obstacles=[]
roadrect=[]
for i in range(5):
    roadrect.append(rrect(-100+150*i))

class Coin():
    def __init__(self, x=10, y=10,  width=30, height=30, speed=18, dx=5):
        self.x = x
        self.y = y
        self.dx=random.randint(-10,10)
        self.speed = speed
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(pygame.transform.scale(
            pygame.image.load('coin.png'), (self.width, self.height)), (self.x, self.y))
        if self.hitbox.colliderect(car.hitbox):
            screen.blit(pygame.transform.scale(
                pygame.image.load('star.png'), (self.width, self.height)), (self.x, self.y))
    def fall(self):
        global score1
        self.x+=self.dx
        self.y += self.speed
        if self.x + self.width > start + road_w or self.x < start: 
            self.dx*=-1
        if self.hitbox.colliderect(car.hitbox):
            pygame.mixer.music.load('bonus.wav')
            pygame.mixer.music.play(1)
            obstacles.remove(self)
            score1 += 1
        elif self.y > sc_height:
            obstacles.remove(self)


def spawner():
    if len(obstacles) < 3:
        coin = Coin(random.randrange(start,road_w + start - 30,20), random.randrange(-110, -10, 10))
        obstacles.append(coin)

def live(score):
    for i in range(3-score):
        table.blit(pygame.transform.scale(
            pygame.image.load('heart.png'), (20, 20)), (21*i, 39))


gameover = False

pygame.mixer.Sound("background.wav").play(-1)

while not gameover:
    spawner()
    screen.blit(pygame.transform.scale(
        pygame.image.load('flower.png'), (sc_width, sc_height)),(0,0))
    pygame.draw.rect(screen,(156,148,148),pygame.Rect(start,0,road_w,road_h))
    
    screen.blit(table,(5,5))
    table.fill((255,255,255))
    
    for r in roadrect:
        r.draw()
        r.fall()
    
    car.draw()
    car.move()
    
    evilcar.draw()
    evilcar.fall()

    for obs in obstacles:
        obs.draw()
        obs.fall()
    
    font = pygame.font.SysFont('ComicSans', 30)
    text = font.render(f'Score:{score1}', 1, (0, 0, 0))
    table.blit(text, (0, 0))
    text1 = font.render(f'Level:{case}', 1, (0, 0, 0))
    table.blit(text1, (0, 20))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    live(score)

    if level//7 == case :
        case+=1
        s = pygame.Surface((sc_width,sc_height))
        s.set_alpha(128)
        s.fill((0,0,0))
        screen.blit(s, (0,0))
        font = pygame.font.SysFont('ComicSans', 40)
        screen.blit(font.render(f'Level:{case}', 1, (255, 255, 255)), (sc_width/2-40,sc_height/2))
        pygame.display.update()
        time.sleep(2)

    if score >= 3:
        gameover = True
        s = pygame.Surface((sc_width,sc_height))
        s.set_alpha(128)
        s.fill((0,0,0))
        screen.blit(s, (0,0))
        screen.blit(game_over, (sc_width//4,sc_height/2-70))
        screen.blit(font.render(f'Score:{score1}', 1, (255, 255, 255)), (sc_width/2,sc_height/2))
        pygame.display.update()
        time.sleep(5)
    
    clock.tick(60)
    pygame.display.update()
