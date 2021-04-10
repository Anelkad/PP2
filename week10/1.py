import pygame
import random
import time

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Game")

sc_height = 600
sc_width = 600
screen = pygame.display.set_mode((sc_width,sc_height))
screen.fill((255,255,255))
road_w = sc_width*2//3
road_h = sc_height

font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, (0,0,0))

score = 0
score1 = 0 

pygame.display.set_caption("Game")

class Enemy:
    def __init__(self,  width=32, height=64):
        self.x = random.randint(sc_width//5,road_w + sc_width//5)
        self.y = 0
        self.speed = random.randrange(5,35,5)
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(pygame.transform.scale(
            pygame.image.load('Enemy.png'), (self.width, self.height)), (self.x, self.y))

    def fall(self):
        global score
        self.y += self.speed
        if self.y > sc_height + self.height:
            self.y = - self.height
            self.x = random.randint(sc_width//5,road_w + sc_width//5 - self.width)
            self.speed = random.randrange(5,35,5)
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

class Car:
    def __init__(self,  width=32, height=64, speed=18):
        self.width = width
        self.height = height
        self.speed = speed
        self.x = sc_width//5 + road_w//2
        self.y = sc_height - self.height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(pygame.transform.scale(
            pygame.image.load('Player.png'), (self.width, self.height)), (self.x, self.y))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT]:
            if self.x + self.width*3/2 < road_w + sc_width//5:
                self.x+=self.speed
        if pressed_keys[pygame.K_LEFT]:
            if self.x - self.width/2 > sc_width//5:
                self.x-=self.speed
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

car = Car()
evilcar = Enemy()

class Coin():
    def __init__(self, x=10, y=10,  width=30, height=30, speed=18):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(pygame.transform.scale(
            pygame.image.load('coin.png'), (self.width, self.height)), (self.x, self.y))

    def fall(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        global score1
        self.y += self.speed
        if self.hitbox.colliderect(car.hitbox):
            obstacles.remove(self)
            score1 += 1
        elif self.y > sc_height:
            obstacles.remove(self)


def drawScore():
    global score1
    font = pygame.font.SysFont('ComicSans', 30)
    text = font.render(f'Score:{score1}', 1, (0, 0, 255))
    screen.blit(text, (10, 20))

def spawner():
    if len(obstacles) < 3:
        coin = Coin(random.randrange(sc_width//5,road_w + sc_width//5 - 30,20), random.randrange(-110, -10, 10))
        obstacles.append(coin)

obstacles=[]

gameover = False

pygame.mixer.Sound("background.wav").play(-1)

while not gameover:
    spawner()
    screen.blit(pygame.transform.scale(pygame.image.load('flower.png'), (sc_width, sc_height)),(0,0))
    screen.blit(pygame.transform.scale(pygame.image.load('road.png'), (road_w, road_h)),(sc_width//5,0))
    
    car.draw()
    car.move()
    
    evilcar.draw()
    evilcar.fall()

    for obs in obstacles:
        obs.draw()
        obs.fall()
    
    drawScore()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

    if car.hitbox.colliderect(evilcar.hitbox):
        gameover = True
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        screen.fill((255,0,0))
        screen.blit(game_over, (30,250))
        screen.blit(font.render(f'Score:{score1}', 1, (255, 255, 255)), (30,290))
        pygame.display.update()
        time.sleep(2)
    
    clock.tick(60)
    pygame.display.update()


