import pygame
import math

pygame.init()

# RGB (255, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (800, 500)
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
screen.fill(WHITE)

pygame.draw.rect(screen, BLACK, pygame.Rect(79, 39, 702, 402))

rec=pygame.Surface((700,400))
rec.fill(WHITE)


pygame.display.set_caption("Graph")

x = 0
y=200-180*math.sin(-350/30)
x0 = 0
y0=200-180*math.cos(-350/30)
i=349

pygame.draw.line(rec, BLACK,[0, 200],[700,200],2)
pygame.draw.line(rec, BLACK,[350, 0],[350,400],2)

for i in range(1,11):
    pygame.draw.line(rec, BLACK,[int((i-4)*math.pi*30)+350, 0],[int((i-4)*math.pi*30)+350,400])
for i in range(1,22):
    pygame.draw.line(rec, BLACK,[int((i-8)*math.pi*15)+350, 0],[int((i-8)*math.pi*15)+350,10])
    pygame.draw.line(rec, BLACK,[int((i-8)*math.pi*15)+350, 390],[int((i-8)*math.pi*15)+350,400])
for i in range(1,22):
    pygame.draw.line(rec, BLACK,[(i-8)*math.pi*15+350+int(math.pi*30)//4, 395],[(i-8)*math.pi*15+350+int(math.pi*30)//4,400])

for i in range(1,12):
    pygame.draw.line(rec, BLACK,[0, 200+(i-6)*45],[700,200+(i-6)*45])
for i in range(1,24):
    pygame.draw.line(rec, BLACK,[0, 200+(i-12)*45//2],[10,200+(i-12)*45//2])
    pygame.draw.line(rec, BLACK,[690, 200+(i-12)*45//2],[700,200+(i-12)*45//2])
for i in range(1,24):
    pygame.draw.line(rec, BLACK,[0, 200+(i-12)*45//2+45//4],[5,200+(i-12)*45//2+45//4])

font = pygame.font.SysFont('Calibri', 15, False, True)
t1=['1.00','0.75','0.5','0.25','0.00','-0.25','-0.5','-0.75','-1.00']
for i in range(9):
    text = font.render(t1[i], True, BLACK)
    screen.blit(text, (40, 50+i*45))
t2=[' -3π ','-5π/2',' -2π ','-3π/2',' -π  ',' -π/2','  0  ',' π/2 ','  π','3π/2','2π','5π/2','3π']
for i in range(13):
    text = font.render(t2[i], True, BLACK)
    screen.blit(text, (125+i*49,450))

done = False
while not done:
    for i in range(-349,351):
     x1=x+1
     y1=200-180*math.sin(i/30)
     pygame.draw.aaline(rec, RED,[x, y],[x1,y1])
     x=x1
     y=y1
     x2=x0+1
     y2=200-180*math.cos(i/30)
     if x2%2==0: pygame.draw.aaline(rec, BLUE,[x0, y0],[x2,y2])
     x0=x2
     y0=y2
     clock.tick(90)
     screen.blit(rec,(80,40))
     pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    