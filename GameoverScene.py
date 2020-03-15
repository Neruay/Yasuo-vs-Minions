from SceneBase import SceneBase
import GameScene
import TitleScene
from Constants import *
from Utils import draw_text
from Utils import button
import pygame

class GameoverScene(SceneBase):
    def __init__(self, score):
        SceneBase.__init__(self)
        self.score = score
        self.slain = pygame.image.load("res/slain.png").convert_alpha()
        self.slain = pygame.transform.scale(self.slain, (round(WINDOW_WIDTH/1.7), round(WINDOW_HEIGHT/5)))
        self.go_bg = pygame.image.load("res/go_bg.png").convert()
        self.go_bg = pygame.transform.scale(self.go_bg, (round(WINDOW_WIDTH), round(WINDOW_HEIGHT)))

    def process_input(self, events, pressed_keys):
        pass

    def update(self):
        pass

    def replay(self):
        self.switch_to_scene(GameScene.GameScene())
    
    def menu(self):
        self.switch_to_scene(TitleScene.TitleScene())

    def game_exit(self):
        self.terminate()

    def render(self, window_surface):
        font = pygame.font.SysFont("comicsansms", round(WINDOW_WIDTH/50))
        scorefont = pygame.font.SysFont("comicsansms", round(WINDOW_WIDTH/18))
        window_surface.blit(self.go_bg, [0, 0])
        window_surface.blit(self.slain, (round(WINDOW_WIDTH/4.7), round(WINDOW_HEIGHT/5)))
        draw_text(f'Score: {self.score}', scorefont, window_surface, round(
            WINDOW_WIDTH/2), round(WINDOW_HEIGHT/2), window_surface, APRICOT)
        button("Retry",font,window_surface,round(WINDOW_WIDTH/3),round(WINDOW_HEIGHT/1.25),round(WINDOW_WIDTH/7.7),round(WINDOW_HEIGHT/12),APRICOT,GOLDEN, self.replay)
        button("Back to menu",font,window_surface,round(WINDOW_WIDTH/1.5-WINDOW_WIDTH/7.7),round(WINDOW_HEIGHT/1.25),round(WINDOW_WIDTH/7.7),round(WINDOW_HEIGHT/12),APRICOT,GOLDEN, self.menu)