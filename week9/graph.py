import pygame
import math

pygame.init()

class Point:
    # constructed using a normal tupple
    def __init__(self, point_t = (0,0)):
        self.x = float(point_t[0])
        self.y = float(point_t[1])
    # define all useful operators
    def __add__(self, other):
        return Point((self.x + other.x, self.y + other.y))
    def __sub__(self, other):
        return Point((self.x - other.x, self.y - other.y))
    def __mul__(self, scalar):
        return Point((self.x*scalar, self.y*scalar))
    def __div__(self, scalar):
        return Point((self.x/scalar, self.y/scalar))
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
    # get back values in original tuple format
    def get(self):
        return (self.x, self.y)
def draw_dashed_line(surf, color, start_pos, end_pos, width=1, dash_length=4):
    origin = Point(start_pos)
    target = Point(end_pos)
    displacement = target - origin
    length = len(displacement)
    slope = displacement.__div__(length)
    for index in range(0, int(length/dash_length), 2):
        start = origin + (slope *    index    * dash_length)
        end   = origin + (slope * (index + 1) * dash_length)
        pygame.draw.line(surf, color, start.get(), end.get(), width)


# RGB (255, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#экран создать
size = (800, 500)
screen = pygame.display.set_mode(size)
screen.fill(WHITE)
clock = pygame.time.Clock()

#граница для графика
pygame.draw.rect(screen, BLACK, pygame.Rect(79, 39, 702, 402),5)

#область для графика
rec=pygame.Surface((700,400))
rec.fill(WHITE)
pygame.display.set_caption("Graph")

#начальные координаты для графика
a=-350
x = 0
y=200-180*math.sin(a/30)
x0 = 0
y0=200-180*math.cos(a/30)

#линии 0X 0Y жирным
pygame.draw.line(rec, BLACK,[0, 200],[700,200],2)
pygame.draw.line(rec, BLACK,[350, 0],[350,400],2)

#рисовка клеток и мелких делений
for i in range(1,11):
    pygame.draw.line(rec, BLACK,[int((i-4)*math.pi*30)+350, 0],[int((i-4)*math.pi*30)+350,400])
for i in range(1,22):
    pygame.draw.line(rec, BLACK,[int((i-8)*math.pi*15)+350, 0],[int((i-8)*math.pi*15)+350,10])
    pygame.draw.line(rec, BLACK,[int((i-8)*math.pi*15)+350, 390],[int((i-8)*math.pi*15)+350,400])
for i in range(1,22):
    pygame.draw.line(rec, BLACK,[(i-8)*math.pi*15+350+int(math.pi*30)//4, 395],[(i-8)*math.pi*15+350+int(math.pi*30)//4,400])
    pygame.draw.line(rec, BLACK,[(i-8)*math.pi*15+350+int(math.pi*30)//4, 0],[(i-8)*math.pi*15+350+int(math.pi*30)//4,5])

for i in range(1,12):
    pygame.draw.line(rec, BLACK,[0, 200+(i-6)*45],[700,200+(i-6)*45])
for i in range(1,24):
    pygame.draw.line(rec, BLACK,[0, 200+(i-12)*45//2],[10,200+(i-12)*45//2])
    pygame.draw.line(rec, BLACK,[690, 200+(i-12)*45//2],[700,200+(i-12)*45//2])
for i in range(1,24):
    pygame.draw.line(rec, BLACK,[0, 200+(i-12)*45//2+45//4],[5,200+(i-12)*45//2+45//4])
    pygame.draw.line(rec, BLACK,[695, 200+(i-12)*45//2+45//4],[700,200+(i-12)*45//2+45//4])

#числовая отметка
font = pygame.font.SysFont('Calibri', 15, False, True)
t1=['1.00','0.75','0.5','0.25','0.00','-0.25','-0.5','-0.75','-1.00']
for i in range(9):
    text = font.render(t1[i], True, BLACK)
    screen.blit(text, (40, 50+i*45))

t2=[' -3π ','-5π/2',' -2π ','-3π/2',' -π  ',' -π/2','  0  ',' π/2 ','  π','3π/2','2π','5π/2','3π']
for i in range(13):
    text = font.render(t2[i], True, BLACK)
    screen.blit(text, (125+i*49,450))

s=font.render('sin(x)',True,BLACK)
screen.blit(s,(20,440))
pygame.draw.line(screen,RED,[55,448],[80,448])

c=font.render('cos(x)',True,BLACK)
screen.blit(c,(20,460))
draw_dashed_line(screen,BLUE,(55,468),(80,468))

font = pygame.font.SysFont('Calibri', 20, False, True)
xx=font.render("X",True,BLACK)
screen.blit(xx,(423,470))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if a<350: a+=1
    x1=x+1
    y1=200-180*math.sin(a/30)
    pygame.draw.aaline(rec, RED,[x, y],[x1,y1]) #sin
    x=x1
    y=y1

    x2=x0+1
    y2=200-180*math.cos(a/30)
    if x0%2==0: pygame.draw.aaline(rec, BLUE,[x0, y0],[x2,y2]) #cos
    x0=x2
    y0=y2

    clock.tick(90)
    screen.blit(rec,(80,40))
    pygame.display.update()
    
    