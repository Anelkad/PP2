import pygame
import random
import pickle
import time
import os

pygame.init()

level = 1
clock = pygame.time.Clock()
#размер экрана
sc_width = 600
sc_height = 400
sc = pygame.display.set_mode((sc_width,sc_height))
table = pygame.Surface((90,30))#для очков поле


pygame.display.set_caption("Snake game")
font = pygame.font.SysFont('ComicSans', 30)

#класс для элементов хвоста
class Circle():
    def __init__(self, x = 0, y = 0):
        self.r = 5
        self.x = x
        self.y = y
        self.speed = 10
        self.hitbox = pygame.Rect(self.x-self.r,self.y-self.r,self.r*2,self.r*2)

    def draw(self):
        pygame.draw.circle(sc,(100,100,100),(self.x,self.y),self.r)

#класс для стен
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
#функция создания карт
def create_map(level):
    with open(f'maps/map_{level}.txt', mode='r') as file:
        row_num = 0 
        for row in file:
            for block_num in range(len(row)):
                if row[block_num] == '1':
                    walls.append(Wall(block_num*20, row_num*20))
            row_num += 1

#класс для головы змеи
class Snakehead():
    def __init__(self):
        self.r = 5
        self.x = 15
        self.y = 15
        self.speed = 10
        self.up = False
        self.down = False
        self.right = False
        self.left = False
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

        keys = pygame.key.get_pressed()    
        if keys[pygame.K_RIGHT] and not self.left:
            self.right = True
            self.up = self.down = self.left = False
        elif keys[pygame.K_LEFT] and not self.right:
            self.left = True
            self.up = self.down = self.right = False
        elif keys[pygame.K_UP] and not self.down:
            self.up = True
            self.down = self.right = self.left = False
        elif keys[pygame.K_DOWN] and not self.up:
            self.down = True
            self.up = self.right = self.left = False

        if self.right:
            self.dx = self.speed
            self.dy = 0
        elif self.left:
            self.dx = -self.speed
            self.dy = 0
        elif self.up:
            self.dx = 0
            self.dy = -self.speed
        elif self.down:
            self.dx = 0
            self.dy = self.speed
        self.y+=self.dy
        self.x+=self.dx
        self.hitbox = pygame.Rect(self.x-self.r,self.y-self.r,self.r*2,self.r*2)

#класс для фрукта
class Fruit():
    def __init__(self):
        self.r = 5
        self.x = random.randrange(5,sc_width-5,10)
        self.y = random.randrange(5,sc_height-5,10)
        self.hitbox = pygame.Rect(self.x-self.r,self.y-self.r,self.r*2,self.r*2)

    def draw(self):
        pygame.draw.circle(sc,(200,10,10),(self.x,self.y),self.r)

eviltail = []   
# класс для второй змеи (другая консоль)     
class evilSnake(Snakehead):
    def __init__(self):
        Snakehead.__init__(self)
        self.r = 5
        self.x = sc_width-15
        self.y = sc_height-15
        self.dx = 0

    def move(self):
        if len(eviltail)>0:
            for i in range(len(eviltail)-1):
                eviltail[i]=Circle(eviltail[i+1].x,eviltail[i+1].y)
            eviltail[len(eviltail)-1]=Circle(self.x,self.y)

        keys = pygame.key.get_pressed()    
        if keys[pygame.K_d] and not self.left:
            self.right = True
            self.up = self.down = self.left = False
        elif keys[pygame.K_a] and not self.right:
            self.left = True
            self.up = self.down = self.right = False
        elif keys[pygame.K_w] and not self.down:
            self.up = True
            self.down = self.right = self.left = False
        elif keys[pygame.K_s] and not self.up:
            self.down = True
            self.up = self.right = self.left = False

        if self.right:
            self.dx = self.speed
            self.dy = 0
        elif self.left:
            self.dx = -self.speed
            self.dy = 0
        elif self.up:
            self.dx = 0
            self.dy = -self.speed
        elif self.down:
            self.dx = 0
            self.dy = self.speed
        self.y+=self.dy
        self.x+=self.dx
        self.hitbox = pygame.Rect(self.x-self.r,self.y-self.r,self.r*2,self.r*2)

#функция игры на двоих
def supergame():
    head = Snakehead()
    evil = evilSnake()
    global tail, eviltail
    tail = []
    f = Fruit()
    
    score1 = 0
    score2 = 0

    gameover1 = False
    gameover2 = False
    gameclose = False
    while not gameclose:
        sc.fill((0,0,0))
        sc.blit(table,(sc_width-95,5))
        table.fill((255,255,255))
        table.blit(font.render("score1 "+str(score1), 1, (0, 0, 0)), (0,0))
        table.blit(font.render("score2 "+str(score2), 1, (0, 0, 0)), (0,14))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameclose = True

        head.move()
        evil.move()
        if head.y-5<0 or head.y+5>sc_height or head.x-5<0 or head.x+5>sc_width:
            gameover1=True
            gameclose=True
        if evil.y-5<0 or evil.y+5>sc_height or evil.x-5<0 or evil.x+5>sc_width:
            gameover2=True
            gameclose=True
        head.draw()
        evil.draw()

        for c in tail:
            c.draw()
            if head.hitbox.colliderect(c.hitbox):
                gameover1 = True
                gameclose= True
            if evil.hitbox.colliderect(c.hitbox):
                gameover2 = True
                gameclose= True
        for c in eviltail:
            c.draw()
            if evil.hitbox.colliderect(c.hitbox):
                gameover2 = True
                gameclose= True
            if head.hitbox.colliderect(c.hitbox):
                gameover1 = True
                gameclose= True
        
        f.draw()
        if head.hitbox.colliderect(f.hitbox):
            score1+=1
            pygame.mixer.music.load('bonus.wav')
            pygame.mixer.music.play(1)
            f = Fruit()
            tail.append(Circle(head.x,head.y))

        if evil.hitbox.colliderect(f.hitbox):
            score2+=1
            pygame.mixer.music.load('bonus.wav')
            pygame.mixer.music.play(1)
            f = Fruit()
            eviltail.append(Circle(evil.x,evil.y))
        clock.tick(8)
        pygame.display.update()

    if gameover1 or gameover2:
        s = pygame.Surface((sc_width,sc_height))
        s.set_alpha(128)
        s.fill((200,0,0))
        sc.blit(s, (0,0))
        pygame.mixer.music.load('gameover.wav')
        pygame.mixer.music.play(1)
        if gameover1: text = font.render("2nd Winner!", True, (0,0,0))
        else: text = font.render("1st Winner!", True, (0,0,0))
        sc.blit(text, (sc_width//4,sc_height/2-70))
        sc.blit(font.render("press F to play again", 1, (255, 255, 255)), (sc_width/2-30,sc_height/2+40))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    supergame()
        pygame.display.update()
        time.sleep(7)

#основная игра с уровнями
def main():
    global tail, walls, level
    level = 1
    score = 0
    FPS = 8
    f = Fruit()
    tail=[]
    head = Snakehead()
    gameover = False
    gameclose = False
    prev = False
    while not gameclose:
        #загрузка предыдущей игры в зависимости от выбора
        while not prev:
            s = pygame.Surface((sc_width,sc_height))
            s.set_alpha(128)
            s.fill((0,0,200))
            sc.blit(s, (0,0))
            sc.blit(font.render("CONTINUE GAME?", 1, (255, 0, 0)), (sc_width//3,sc_height/2))
            sc.blit(font.render("Yes: press y / No: press n", 1, (0, 0, 0)), (sc_width//3,sc_height/2+50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    prev=True
                    gameclose = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        pickle_out = open("f.pickle","rb")
                        ex = pickle.load(pickle_out)
                        score = ex["score"]
                        level = ex["level"]
                        FPS = ex["fps"]
                        f = ex["fruit"]
                        tail = [Circle(head.x,head.y) for i in range(ex["len"])]
                        prev=True
                    if event.key ==pygame.K_n:
                        prev=True

        sc.fill((0,0,0))
        create_map(level)
        sc.blit(table,(sc_width-95,5))
        table.fill((255,255,255))
        table.blit(font.render("score "+str(score), 1, (0, 0, 0)), (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameclose = True
                
        head.move()
        if head.y-5<0 or head.y+5>sc_height or head.x-5<0 or head.x+5>sc_width:
            gameover=True
            gameclose=True
        head.draw()

        for w in walls:
            w.draw()
            if head.hitbox.colliderect(w.hitbox):
                gameover = True
                gameclose= True
            if f.hitbox.colliderect(w.hitbox):
                f = Fruit()
        for c in tail:
            c.draw()
            if head.hitbox.colliderect(c.hitbox):
                gameover = True
                gameclose= True
        
        f.draw()
        if head.hitbox.colliderect(f.hitbox):
            score+=1
            pygame.mixer.music.load('bonus.wav')
            pygame.mixer.music.play(1)
            f = Fruit()
            tail.append(Circle(head.x,head.y))

        if score//10 ==level:
            pygame.mixer.music.load('level.wav')
            pygame.mixer.music.play(1)
            FPS+=1
            level+=1
            walls = []
            tail = []
            head = Snakehead()
            if level >=6:
                s = pygame.Surface((sc_width,sc_height))
                s.set_alpha(128)
                s.fill((0,0,200))
                sc.blit(s, (0,0))
                sc.blit(font.render("WINNER!", 1, (255, 255, 255)), (sc_width/2-40,sc_height/2))
                pygame.display.update()
                time.sleep(2)
                return
            else:
                s = pygame.Surface((sc_width,sc_height))
                s.set_alpha(128)
                s.fill((0,0,200))
                sc.blit(s, (0,0))
                sc.blit(font.render("LEVEL "+str(level), 1, (255, 255, 255)), (sc_width/2-40,sc_height/2))
                pygame.display.update()
                time.sleep(2)
        
        clock.tick(FPS)
        pygame.display.update()

    if gameover:
        s = pygame.Surface((sc_width,sc_height))
        s.set_alpha(128)
        s.fill((200,0,0))
        sc.blit(s, (0,0))
        pygame.mixer.music.load('gameover.wav')
        pygame.mixer.music.play(1)
        sc.blit(font.render("GAME OVER", True, (0,0,0)), (sc_width//4,sc_height/2-70))
        sc.blit(font.render("Score : "+str(score), 1, (255, 255, 255)), (sc_width/2-30,sc_height/2))
        sc.blit(font.render("press F to play again", 1, (255, 255, 255)), (sc_width/2-30,sc_height/2+40))
        pygame.display.update()
        time.sleep(7)
        if level<6:
            dic = {
            "score" : score,
            "level" : level,
            "fps" : FPS,
            "len" : len(tail),
            "fruit" : f
            }
            pickle_out = open("f.pickle","wb")
            pickle.dump(dic,pickle_out)
            pickle_out.close()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    main()

    
pygame.mixer.Sound("background.wav").play(-1)
#запуск игры в зависимости от выбора
run = False
while not run:
    s = pygame.Surface((sc_width,sc_height))
    s.set_alpha(128)
    s.fill((0,0,200))
    sc.blit(s, (0,0))
    sc.blit(font.render("Game for 2?", 1, (255, 0, 0)), (sc_width//3,sc_height/2))
    sc.blit(font.render("Yes: press y / No: press n", 1, (0, 0, 0)), (sc_width//3,sc_height/2+50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                run=True
                supergame()
            if event.key ==pygame.K_n:
                run=True
                main()

