from SceneBase import SceneBase
import GameScene
import ScoreboardScene
from Constants import *
from Utils import draw_text
from Utils import button
import pygame

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.menubg = pygame.image.load("res/title.png").convert()
        self.menubg = pygame.transform.scale(self.menubg, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.switch_to_scene(GameScene.GameScene())

    def update(self):
        pass
    
    def play(self):
        self.switch_to_scene(GameScene.GameScene())

    def score(self):
        self.switch_to_scene(ScoreboardScene.ScoreboardScene())

    def game_exit(self):
        self.terminate()

    def render(self, window_surface):
        font = pygame.font.SysFont("comicsansms", round(WINDOW_WIDTH/30))
        window_surface.blit(self.menubg, [0, 0])
        button("PLAY",font,window_surface,round(WINDOW_WIDTH/3-WINDOW_WIDTH/4),round(WINDOW_HEIGHT/3.5),round(WINDOW_WIDTH/4),round(WINDOW_HEIGHT/10),APRICOT,GOLDEN, self.play)
        button("SCOREBOARD",font,window_surface,round(WINDOW_WIDTH/3-WINDOW_WIDTH/4),round(WINDOW_HEIGHT/2.2),round(WINDOW_WIDTH/4),round(WINDOW_HEIGHT/10),APRICOT,GOLDEN, self.score)
        button("Quit",font,window_surface,round(WINDOW_WIDTH/3-WINDOW_WIDTH/4),round(WINDOW_HEIGHT/1.2),round(WINDOW_WIDTH/4),round(WINDOW_HEIGHT/10),APRICOT,GOLDEN, self.game_exit)
        