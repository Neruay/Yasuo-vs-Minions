from random import seed
from random import randint
from Constants import *
import ScoreboardScene
import GameScene
import TitleScene
import datetime
import pygame
import sys 
import time
import math
import os
from pygame.locals import *


def run_game(width, height, fps, starting_scene):
    seed(time)
    clock = pygame.time.Clock()
    active_scene = starting_scene

    while active_scene != None:
        pressed_keys = pygame.key.get_pressed()
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                    pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE and not isinstance(active_scene, ScoreboardScene.ScoreboardScene):
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True

            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)

        active_scene.process_input(filtered_events, pressed_keys)
        active_scene.update()
        active_scene.render(window_surface)

        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN, 0, 32)
    icon = pygame.image.load("res/icon.png").convert()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Yasuo vs Minions')
    run_game(WINDOW_WIDTH, WINDOW_HEIGHT, TICK, TitleScene.TitleScene())