from SceneBase import SceneBase
import TitleScene
import pygame
from pygame.locals import *
from Constants import *
from Utils import draw_text
from Utils import draw_scoreboard


class ScoreboardScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.rankedbg = pygame.image.load("res/ranked.png").convert()
        self.rankedbg = pygame.transform.scale(self.rankedbg, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.currentline = []
        self.indent = WINDOW_HEIGHT/3 - WINDOW_HEIGHT/4
        self.x = 0

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.switch_to_scene(TitleScene.TitleScene())

    def update(self):
        with open("scoreboard.txt", "r") as scoreboard:
            self.x = scoreboard.readlines()
            if self.x != 0:
                self.currentline = list(self.x)

    def render(self, window_surface):
        window_surface.blit(self.rankedbg, [0, 0])
        sbfont = pygame.font.SysFont("comicsansms", round(WINDOW_WIDTH/14))
        helpfont = pygame.font.SysFont("comicsansms", round(WINDOW_WIDTH/40))
        scorefont = pygame.font.SysFont("comicsansms", round(WINDOW_WIDTH/40))
        draw_text('LEADERBOARD', sbfont, window_surface, round(
            WINDOW_WIDTH/2), round(WINDOW_HEIGHT/10), window_surface, GOLDEN)
        draw_text('(press ESC to return)', helpfont, window_surface, round(
            WINDOW_WIDTH/2), round(WINDOW_HEIGHT/5), window_surface, GOLDEN)
        if len(self.x) > 0:
            draw_scoreboard(f'1 - {self.currentline[0]}', scorefont, window_surface, round(
                WINDOW_WIDTH/11), round(WINDOW_HEIGHT/3), window_surface)
        if len(self.x) > 1:
            draw_scoreboard(f'2 - {self.currentline[1]}', scorefont, window_surface, round(
                WINDOW_WIDTH/11), round(WINDOW_HEIGHT/3 + self.indent), window_surface)
        if len(self.x) > 2:
            draw_scoreboard(f'3 - {self.currentline[2]}', scorefont, window_surface, round(
                WINDOW_WIDTH/11), round(WINDOW_HEIGHT/3 + self.indent*2), window_surface)
        if len(self.x) > 3:
            draw_scoreboard(f'4 - {self.currentline[3]}', scorefont, window_surface, round(
                WINDOW_WIDTH/11), round(WINDOW_HEIGHT/3 + self.indent*3), window_surface)
        if len(self.x) > 4:
            draw_scoreboard(f'5 - {self.currentline[4]}', scorefont, window_surface, round(
                WINDOW_WIDTH/11), round(WINDOW_HEIGHT/3 + self.indent*4), window_surface)
