from random import seed
from random import randint
import pygame, sys, time, math
from pygame.locals import * 

seed(time)

def DrawText(text, font, surface_menu, x, y, selected=False):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    windowSurface.blit(textobj, textrect)


pygame.init()

WINDOWWIDTH = 1200
WINDOWHEIGHT = 800
font_color = (255, 255, 153)
font = pygame.font.SysFont("comicsansms", 72)
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')
fps = pygame.time.Clock()

MOVESPEED = 5

WHITE = (255, 255, 255),
GRAY = (51, 51, 51),
RED = (255, 0, 0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255) 
BLACK = (0, 0, 0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)
AZURE = (240,255,255)
OLIVE = (128,128,0)

CIRCLERADIUS = 100
QUANTITY = 10

class Circle(object):
    def __init__(self, x, y, radius, color, duration, direction, dx, dy):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.duration = duration
        self.direction = direction
        self.dx = dx
        self.dy = dy

    def intersects(self, circle):
        return (self.x - circle.x)**2 + (self.y - circle.y)**2 < (self.radius + circle.radius)**2

def generate_circle_random_pos():
    colors = [RED, GREEN, BLUE, CYAN, MAGENTA, AZURE, OLIVE]
    x = randint(CIRCLERADIUS, WINDOWWIDTH-CIRCLERADIUS)
    y = randint(CIRCLERADIUS, WINDOWHEIGHT-CIRCLERADIUS)
    return Circle(x, y, CIRCLERADIUS, colors[randint(0, len(colors)-1)], 0, 0, 0, 0)

def generate_circles(num_circles):
    circles = []
    while len(circles) < num_circles:
        new_circle = generate_circle_random_pos()
        has_intersection = False
        for c in circles:
            if c.intersects(new_circle):
                has_intersection = True
                break
        if not has_intersection:
            circles.append(new_circle)
    return circles

circles = generate_circles(QUANTITY)

MOVESPEED = 5

DX = [-MOVESPEED, 0, MOVESPEED, 0, -MOVESPEED, MOVESPEED, MOVESPEED, -MOVESPEED]
DY = [0, -MOVESPEED, 0, MOVESPEED, -MOVESPEED, -MOVESPEED, MOVESPEED, MOVESPEED]

lastposx = 0
lastposy = 0

while True:
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(GRAY)

    DrawText('Start', font, windowSurface, (WINDOWWIDTH/2) -
         100, (WINDOWHEIGHT/2)-110, True)
    DrawText('Options', font, windowSurface,
         (WINDOWWIDTH/2)-100, (WINDOWHEIGHT/2)-40)
    DrawText('Quit', font, windowSurface,
         (WINDOWWIDTH/2)-100, (WINDOWHEIGHT/2)+30)

    for c in circles:
        if c.duration == 0:
            c.duration = randint(25, 100)
            check = c.direction
            c.direction = randint(0, 7)
            while check == c.direction:
                c.direction = randint(0, 7)
        if c.x + DX[c.direction] + c.radius < WINDOWWIDTH and c.x + DX[c.direction] - c.radius > 0 and c.y + DY[c.direction] + c.radius < WINDOWHEIGHT and c.y + DY[c.direction] - c.radius > 0:
            c.dx = DX[c.direction]
            c.dy = DY[c.direction]
        else:
            while c.x + DX[c.direction] + c.radius >= WINDOWWIDTH or c.x + DX[c.direction] - c.radius <= 0 or c.y + DY[c.direction] + c.radius >= WINDOWHEIGHT or c.y + DY[c.direction] - c.radius <= 0:
                c.direction = randint(0, 7)
            c.dx = DX[c.direction]
            c.dy = DY[c.direction]
        lastposx = c.x
        lastposy = c.y
        c.x += c.dx
        c.y += c.dy
        c.duration -= 1  
        pygame.draw.circle(windowSurface, c.color, (c.x,c.y), c.radius, 15)
    pygame.display.update()
    fps.tick(60)
