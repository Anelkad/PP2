# Paint
import pygame, random

# (x1, y1), (x2, y2)
# A = y2 - y1
# B = x1 - x2
# C = x2 * y1 - x1 * y2
# Ax + By + C = 0
# (x - x1) / (x2 - x1) = (y - y1) / (y2 - y1)

#рисовка ровной линии
def drawLine(screen, start, end, width, color,tool):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            if tool==0:pygame.draw.circle(screen, color, (x, y), width)
            if tool==3:pygame.draw.rect(screen,(0,0,0),(x,y,width,width))
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            if tool==0:pygame.draw.circle(screen, color, (x, y), width)
            if tool==3:pygame.draw.rect(screen,(0,0,0),(x,y,width,width))

#рисовка круга отноосительно куда тянется курсор
def drawCicrle(screen,start,end,color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)

    d=dx
    if y1>y2:
        a=y1-d//2
    else:
        a=y1+d//2
    pygame.draw.circle(screen,color,(min(x1,x2)+d//2,a),d//2)

sc_width = 800
sc_height = 600
screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Paint game")
s = pygame.Surface((sc_width,sc_height))#плоскость где будет рисунок

def main():
    s.fill((0,0,0))
    screen.blit(s, (0,0))
    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)

    dr=5
    radius = 1

    currentTool = 0 # текущий инструмент
    toolCount = 4

    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'yellow': (255,255,0),
        'pink': (255,0,255)
    }

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_b:
                    mode = 'blue'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_p:
                    mode = 'pink'
                if event.key == pygame.K_y:
                    mode = 'yellow'
                if event.key == pygame.K_r:
                    mode = 'random'
                if event.key == pygame.K_UP:
                    radius += dr
                if event.key == pygame.K_DOWN:
                    if radius>dr: radius -= dr
                if event.key == pygame.K_n:
                    radius = 1
                    dr = 5
                    currentTool = (currentTool + 1) % toolCount
                    if currentTool==3:
                        radius = 10
                        dr = 10
                if event.key == pygame.K_s:
                    pygame.image.save(s,'image.jpg')

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]

                if currentTool == 0: pygame.draw.circle(s, color, event.pos, radius)
                if currentTool == 3: pygame.draw.rect(s,(0,0,0),(event.pos[0],event.pos[1],radius,radius)) 
                
                first_pos = event.pos
                draw_on = True

            if event.type == pygame.MOUSEBUTTONUP:
                last_pos = event.pos
                if currentTool == 1:
                    pygame.draw.rect(s,color,(min(first_pos[0],last_pos[0]),
                    min(first_pos[1],last_pos[1]),abs(first_pos[0]-last_pos[0]),abs(first_pos[1]-last_pos[1])))
                if currentTool == 2:
                    drawCicrle(s,first_pos,last_pos,color)
                screen.blit(s, (0,0))
                draw_on = False
            if event.type == pygame.MOUSEMOTION:

                screen.blit(s, (0,0))# изменение будет рисоватся поверх
                if draw_on:
                    if currentTool == 1:
                        pygame.draw.rect(screen,color,(min(first_pos[0],last_pos[0]),
                            min(first_pos[1],last_pos[1]),abs(first_pos[0]-last_pos[0]),abs(first_pos[1]-last_pos[1])))
                    if currentTool == 2:
                        drawCicrle(screen,first_pos,last_pos,color)
                    if currentTool==0 or currentTool==3:
                        drawLine(s, last_pos, event.pos, radius, color,currentTool)

                last_pos = event.pos
                pygame.display.flip()
        pygame.display.flip()

    pygame.quit()

main()