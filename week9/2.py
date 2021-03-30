import pygame
import math

pygame.init()

# RGB (255, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (700, 500)

screen = pygame.display.set_mode(size)
screen.fill(WHITE)

pygame.display.set_caption("Graph")

x = 0
y=250-180*math.sin(-350/30)
x0 = 0
y0=250-180*math.cos(-350/30)
i=349

pygame.draw.line(screen, BLACK,[0, 250],[700,250],2)
pygame.draw.line(screen, BLACK,[350, 0],[350,500],2)

for i in range(1,5):
    pygame.draw.line(screen, BLACK,[int(i*math.pi*30)+350, 0],[int(i*math.pi*30)+350,500])
for i in range(1,5):
    pygame.draw.line(screen, BLACK,[-int(i*math.pi*30)+350, 0],[-int(i*math.pi*30)+350,500])

for i in range(1,6):
    pygame.draw.line(screen, BLACK,[0, 250-i*45],[700,250-i*45])
for i in range(1,6):
    pygame.draw.line(screen, BLACK,[0, 250+i*45],[700,250+i*45])

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    for i in range(-349,350):
     x1=x+1
     y1=250-180*math.sin(i/30)
     pygame.draw.line(screen, RED,[x, y],[x1,y1],2)
     x=x1
     y=y1
    for i in range(-349,350):
     x2=x0+1
     y2=250-180*math.cos(i/30)
     pygame.draw.line(screen, BLUE,[x0, y0],[x2,y2],2)
     x0=x2
     y0=y2
    pygame.display.update()

pygame.quit()