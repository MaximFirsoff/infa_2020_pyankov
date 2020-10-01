import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 530))

def bird(a,b,c):
    Q=[]
    W=[]
    for i in range (a,a+15*c,1):
        Q.append((i,(0.15/c)*(i-a-10*c)**2+b-15*c))
        W.append((2*a-i,(0.15/c)*(i-a-10*c)**2+b-15*c))
    for i in range(a+1,a+15,-1):
        Q.append((i,(1/20/c)*(i-a-15*c)**2+b-11.25*c))
        W.append((2*a-i,(1/20/c)*(i-a-15*c)**2+b-11.25*c))
    polygon(screen, (64,27,3),Q)
    polygon(screen, (64,27,3),W)
    Q=[]
    W=[]

        

rect(screen, (254, 214, 163), (0, 0, 800, 530))
rect(screen, (254, 214, 197), (0, 110, 800, 230))
circle(screen, (252, 239, 27), (400,50), 40)

polygon(screen, (252,153,45), [(165,108), (196,119), (205,140), (307,204), (360,195), (387,209), (165,230)])
polygon(screen, (252,153,45),[(387,209), (429,107), (463,182), (480,161), (480,200)])

D=[]
for i in range(480,600,1):
    D.append((i, (-25/3481)*(i-480)**2+161))
D.append ((600,189))
D.append ((480,200))
polygon(screen, (252, 153, 45), D)

F=[]
for i in range(0,165,1):
    F.append((i, (-109/21904)*(i-17)**2+217))
F.append ((165,230))
F.append ((0,245))
polygon(screen, (252, 153, 45), F)

polygon(screen, (252,153,45),[(579,105), (634,134), (666, 127), (718,155), (750,140), (800,170), (600,189)])

polygon(screen, (173, 65, 49), [(800, 190), (800,340), (655,344), (655,284), (688,240), (720,263), (740, 235), (770, 240)])
polygon(screen, (173, 65, 49), [(459,284), (459,350), (140,360), (140,340), (175,282), (231,311), (260, 240), (325, 255),(385, 300)])

A=[]
for i in range(25,155,1):
    A.append((i, (18/841)*(i-73)**2+214))
A.append ((140,360))
A.append ((25,360))
polygon(screen, (173, 65, 49), A)

B=[]
for i in range(450,565,1):
    B.append((i, (1/125)*(i-550)**2+220))
B.append ((565,360))
B.append ((450,360))
polygon(screen, (173, 65, 49), B)

polygon(screen, (178,125,135), [(0,358), (800,340), (800,530), (0, 530)])

C=[]
for i in range(565,655,1):
    C.append((i, (-59/7921)*(i-655)**2+285))
C.append ((655,360))
C.append ((565,360))
polygon(screen, (173, 65, 49), C)

polygon(screen, (178,125,135), [(0,358), (800,340), (800,530), (0, 530)])

bird(622,426,3)
bird(545,397,2)
bird(636,382,2)
bird(500,360,1)

bird(320,250,1)
bird(380,225,1)
bird(380,200,1)
bird(310,190,1)

polygon(screen, (44,7,33), [(0,200), (95,300), (175,400), (175,530), (0,530)])
polygon(screen, (44,7,33), [(315,525), (380,528), (510,450), (545,470), (545,530), (315,530)])

Z=[]
for i in range(175,315,1):
    Z.append((i, (-5/784)*(i-315)**2+525))
Z.append ((315,530))
Z.append ((175,530))
polygon(screen, (44, 7, 33), Z) 

H=[]
for i in range(545,800,1):
    H.append((i, (-9/3380)*(i-700)**2+500))
H.append ((800,530))
H.append ((545,530))
polygon(screen, (44, 7, 33), H) 

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
