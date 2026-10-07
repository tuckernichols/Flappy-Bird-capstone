import pygame.image
import os
import random

POLE_WIDTH = 300
GAP_BETWEEN_POLES = 150
PIPE_SPEED = 4

top_pipe_img = pygame.image.load(os.path.join("Images/flappy_bird_top_pipe.png"))
top_pipe_img = pygame.transform.scale(top_pipe_img, (POLE_WIDTH, 600))
bottom_pipe_img = pygame.image.load(os.path.join("Images/flappy_bird_bottom_pipe.png"))
bottom_pipe_img = pygame.transform.scale(bottom_pipe_img, (POLE_WIDTH, 600))


class Pipe():
    def __init__(self):
        self.pipe_bottom = random.randint(130, 600)
        self.pipe_top = self.pipe_bottom - GAP_BETWEEN_POLES
        self.x = 950

    def draw_pipe(self, SCREEN):
        SCREEN.blit(top_pipe_img, (self.x, self.pipe_top - 500))
        SCREEN.blit(bottom_pipe_img, (self.x, self.pipe_bottom))
        self.x -= PIPE_SPEED

    def get_bottom(self):
        return self.pipe_bottom + 48

    def get_top(self):
        return self.pipe_top + 53

    def get_x(self):
        return self.x + 112     # pipe img width is 300 real width is around 100


def get_next_pipe(pipe_list):
    for p in pipe_list:
        if p.get_x() + 70 >= 150:           # 150 is bird spawn y
            return p