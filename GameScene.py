from SceneBase import SceneBase
import GameoverScene
import TitleScene
from Circle import Circle
from Constants import *
from Utils import generate_circles
from Utils import draw_text
from Utils import update_leaderboard
from pygame.locals import *
from random import randint
import pygame


class GameScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.player = Circle(
            round(WINDOW_WIDTH/2), round(WINDOW_HEIGHT/2), PLAYER_SIZE, GREEN, 0, 0, 0)
        self.score = 0
        self.moveDown = False
        self.moveUp = False
        self.moveRight = False
        self.moveLeft = False
        self.pause = False
        self.circles = generate_circles(CIRCLES_NUM, self.player)
        self.minions = [pygame.image.load('res/minion_1.png'), pygame.image.load('res/minion_2.png'), pygame.image.load(
            'res/minion_3.png'), pygame.image.load('res/minion_4.png'), pygame.image.load('res/minion_5.png'), pygame.image.load('res/minion_6.png')]
        self.background_image = pygame.image.load("res/bg.png").convert()
        self.background_image = pygame.transform.scale(self.background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def process_input(self, events, pressed_keys):

        for event in events:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w or event.key == K_UP:
                    self.moveDown = False
                    self.moveUp = True
                elif event.key == K_a or event.key == K_LEFT:
                    self.moveRight = False
                    self.moveLeft = True
                elif event.key == K_s or event.key == K_DOWN:
                    self.moveUp = False
                    self.moveDown = True
                elif event.key == K_d or event.key == K_RIGHT:
                    self.moveLeft = False
                    self.moveRight = True
            elif event.type == KEYUP:
                if event.key == K_w or event.key == K_UP:
                    self.moveUp = False
                elif event.key == K_a or event.key == K_LEFT:
                    self.moveLeft = False
                elif event.key == K_s or event.key == K_DOWN:
                    self.moveDown = False
                elif event.key == K_d or event.key == K_RIGHT:
                    self.moveRight = False
                elif event.key == K_SPACE:
                    if self.pause:
                        self.pause = False
                    else:
                        self.pause = True
                        self.moveLeft = False
                        self.moveRight = False
                        self.moveUp = False
                        self.moveDown = False

    def update(self):

        if self.pause:
            return

        self.score += 1
        if self.score % 20 == 0:
            self.player.radius += 1

        if self.moveDown and self.player.y + self.player.radius < WINDOW_HEIGHT:
            self.player.y += MOVESPEED*2
        if self.moveUp and self.player.y - self.player.radius > 0:
            self.player.y -= MOVESPEED*2
        if self.moveLeft and self.player.x - self.player.radius > 0:
            self.player.x -= MOVESPEED*2
        if self.moveRight and self.player.x + self.player.radius < WINDOW_WIDTH:
            self.player.x += MOVESPEED*2

        for c in self.circles:
            if c.intersects(self.player):
                update_leaderboard(self.score)
                self.switch_to_scene(GameoverScene.GameoverScene(self.score))
                break

        new_circles = []

        while True:
            global_ok = True
            for c in self.circles:
                cand = Circle(c.x, c.y, CIRCLE_RADIUS, c.color,
                              c.duration, c.direction, c.sprite)
                chance = randint(1, 100)
                if chance >= 99:
                    cand.set_random_dir()
                cand.make_move()
                ok = True
                for c2 in new_circles:
                    if c2.intersects(cand):
                        ok = False
                        break
                for c2 in self.circles:
                    if c2 != c and c2.intersects(cand):
                        ok = False
                        break
                cnt = 0
                MAX_CNT = 50
                while not ok:
                    cand = Circle(c.x, c.y, CIRCLE_RADIUS, c.color,
                                  c.duration, c.direction, c.sprite)
                    cand.set_random_dir()
                    cand.make_move()
                    ok = True
                    for c2 in new_circles:
                        if c2.intersects(cand):
                            ok = False
                            break
                    for c2 in self.circles:
                        if c2 != c and c2.intersects(cand):
                            ok = False
                            break
                    cnt += 1
                    if cnt == MAX_CNT:
                        break
                if cnt == MAX_CNT:
                    new_circles.clear()
                    global_ok = False
                    break
                new_circles.append(cand)
            if global_ok:
                break
        self.circles = new_circles

    def render(self, window_surface):
        player_image = pygame.image.load('res/player.png').convert_alpha()
        font = pygame.font.SysFont("comicsansms", 72)
        window_surface.blit(self.background_image, [0, 0])
        player_stretched_image = pygame.transform.scale(
            player_image, (self.player.radius*2, self.player.radius*2))
        playerpos = pygame.Rect(
            0, 0, self.player.radius*2, self.player.radius*2)
        playerpos.center = (self.player.x, self.player.y)

        draw_text(f'Score: {self.score}', font, window_surface, round(
            WINDOW_WIDTH/2), round(WINDOW_HEIGHT/10), window_surface, GOLDEN)

        for c in self.circles:
            minion_stretched_image = pygame.transform.scale(
                self.minions[c.sprite], (CIRCLE_RADIUS*2, CIRCLE_RADIUS*2))
            minionpos = pygame.Rect(0, 0, CIRCLE_RADIUS*2, CIRCLE_RADIUS*2)
            minionpos.center = (c.x, c.y)
            window_surface.blit(minion_stretched_image, minionpos)
        window_surface.blit(player_stretched_image, playerpos)
