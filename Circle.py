from Constants import *
from random import randint

class Circle(object):
    def __init__(self, x, y, radius, color, duration, direction, sprite):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.duration = duration
        self.direction = direction
        self.sprite = sprite
        self.DX = [-MOVESPEED, 0, MOVESPEED, 0, -MOVESPEED, MOVESPEED, MOVESPEED, -MOVESPEED]
        self.DY = [0, -MOVESPEED, 0, MOVESPEED, -MOVESPEED, -MOVESPEED, MOVESPEED, MOVESPEED]

    def intersects(self, circle):
        return ((self.x - circle.x)**2 + (self.y - circle.y)**2 <
                (self.radius + circle.radius)**2)

    def check_min_distance(self, circle, min_distance):
        return ((self.x - circle.x)**2 + (self.y - circle.y)**2 <
                (self.radius + circle.radius + min_distance)**2)

    def make_move(self):
        if self.duration == 0:
            self.set_random_dir()
        while (self.x + self.DX[self.direction] + self.radius >= WINDOW_WIDTH or
               self.x + self.DX[self.direction] - self.radius <= 0 or
               self.y + self.DY[self.direction] + self.radius >= WINDOW_HEIGHT or
               self.y + self.DY[self.direction] - self.radius <= 0):
            self.set_random_dir()
        self.x += self.DX[self.direction]
        self.y += self.DY[self.direction]
        self.duration -= 1

    def set_random_dir(self):
        self.duration = randint(50, 150)
        check = self.direction
        self.direction = randint(0, 7)
        while check == self.direction:
            self.direction = randint(0, 7)