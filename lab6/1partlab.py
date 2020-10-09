import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((600, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
fon=0
def new_ball():
    '''рисует новый шарик '''
    global x,y,r,vx,vy
    vx=randint(5, 15)
    vy=randint(5, 15)
    x = randint(100, 600)
    y = randint(100, 600)
    r = randint(10, 50)
    color = COLORS[randint(0, 5)]
    '''if color!=fon:
        x+=1
    elif fon==1:
        color=0
    else: color=1'''
    circle(screen, color, (x, y), r)
    return { 'x':x,
             'y':y,
             'r':r,
             'vx':vx,
             'vy':vy,
             'color':color}


def move(ball):
    if ((ball['x']+ball['r'])<600) and (ball['x']+ball['r'])>0:
        ball ['x']+=ball ['vx']
    else:
        ball['vx']*=-1
        ball['x']+=ball['vx']
    
    if ((ball['y']+ball['r'])<600) and (ball['y']+ball['r'])>0:
        ball ['y']+=ball ['vy']
    else:
        ball['vy']*=-1
        ball['y']+=ball['vy']
    
    circle (screen, ball['color'], ( ball['x'], ball ['y']), ball['r'])


font=pygame.font.Font(None,50)

balls = [new_ball() for _ in range(5)]


sum0=0
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x0,y0=event.pos
            for i in range(0,5,1):
                if (((balls[i]['x']-x0)**2+(balls[i]['y']-y0)**2)**(1/2))<=balls[i]['r'] :
                    sum0+=1
                    balls[i]=new_ball()

                
    #new_ball()
    
    text=font.render(str(sum0),1 ,(255, 255, 255))
    screen.blit (text, (0,0))
    pygame.display.update()
    #fon=COLORS[randint (0,5)]
    screen.fill((255,165,0))
    for i in range (0,5,1):
        move(balls[i])

pygame.quit()
