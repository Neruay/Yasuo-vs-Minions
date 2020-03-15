from Constants import *
from random import randint
from Circle import Circle
from pygame.locals import *
import datetime
import pygame

def update_leaderboard(score):
    buffer = []
    timestamp = datetime.datetime.now()
    now = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    scoreboard = open("scoreboard.txt", "a")
    scoreboard.write(f"{score} | {now}")
    scoreboard.close()
    with open("scoreboard.txt", "r") as scoreboard:
        x = scoreboard.readlines()
        for i in range(len(x)):
            currentline = x[i]
            element = currentline.strip().split(' | ')
            buffer.append((int(element[0]), element[1]))
    buffer.sort(reverse=True)
    file = open("scoreboard.txt", "w")
    file.close()
    scoreboard = open("scoreboard.txt", "a")
    for i in range(len(buffer)):
        scoreboard.write(str(buffer[i][0]) + " | " + buffer[i][1] + '\n')
    scoreboard.close()


def generate_circle_random_pos():
    colors = [RED, GREEN, BLUE, CYAN, MAGENTA, AZURE, OLIVE, GOLDEN]
    x = randint(CIRCLE_RADIUS, WINDOW_WIDTH-CIRCLE_RADIUS)
    y = randint(CIRCLE_RADIUS, WINDOW_HEIGHT-CIRCLE_RADIUS)
    return Circle(x, y, CIRCLE_RADIUS, colors[randint(0, len(colors)-1)], 0, 0, randint(0, 5))


def generate_circles(num_circles, player):
    MIN_DISTANCE = 200
    MAX_CNT = 500
    circles = []
    cnt = 0
    while len(circles) < num_circles:
        new_circle = generate_circle_random_pos()
        if player.check_min_distance(new_circle, MIN_DISTANCE):
            continue
        has_intersection = False
        for c in circles:
            if c.intersects(new_circle):
                has_intersection = True
                break
        if not has_intersection:
            circles.append(new_circle)
        cnt += 1
        if cnt == MAX_CNT:
            circles.clear()
    return circles


def draw_text(text, font, surface_menu, x, y, window_surface, colour):
    textobj = font.render(text, 1, colour)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    window_surface.blit(textobj, textrect)

def draw_scoreboard(text, font, surface_menu, x, y, window_surface):
    textobj = font.render(text, 1, GOLDEN)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    window_surface.blit(textobj, textrect)

def button(msg,font,window_surface,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window_surface, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(window_surface, ic,(x,y,w,h))

    textobj = font.render(msg, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.center = ( (x+(w/2)), (y+(h/2)) )
    window_surface.blit(textobj, textrect)