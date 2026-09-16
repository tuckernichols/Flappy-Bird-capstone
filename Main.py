import random

import pygame
import sys
import os

## UI settings
WIDTH = 1000
HEIGHT = 700

## Game settings
DISTANCE_BETWEEN_POLES = 130
SPEED = 2.1


## imgs
backround_img = pygame.image.load(os.path.join("Images/flappy_bird_backround2.png"))
backround_img = pygame.transform.scale(backround_img, (WIDTH, HEIGHT))

top_pipe_img = pygame.image.load(os.path.join("Images/flappy_bird_top_pipe.png"))
top_pipe_img = pygame.transform.scale(top_pipe_img, (255,600 ))
bottom_pipe_img = pygame.image.load(os.path.join("Images/flappy_bird_bottom_pipe.png"))
bottom_pipe_img = pygame.transform.scale(bottom_pipe_img, (255,600 ))


#
class Pipe():
    x = 950

    def __init__(self):
        self.pipe_bottom = random.randint(130, 600)
        self.pipe_top = self.pipe_bottom - DISTANCE_BETWEEN_POLES

    def draw_pipe(self):
        SCREEN.blit(top_pipe_img, (self.x, self.pipe_top - 500))
        SCREEN.blit(bottom_pipe_img, (self.x, self.pipe_bottom))
        self.x -= SPEED



# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 60

running = True
count = 0
pole_made = False
while running:
    count += 1
    if count > 400:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    # --- Update ---
    SCREEN.blit(backround_img, (0, 0))
    if (pole_made == False):
        pole1 = Pipe()
        pole_made = True
    pole1.draw_pipe()

    #
    # SCREEN.blit(top_pipe_img, (500, -30))
    # SCREEN.blit(bottom_pipe_img, (500, 600))
    #
    # SCREEN.blit(top_pipe_img, (400, -500))
    # SCREEN.blit(bottom_pipe_img, (400, 130))


    # Update player, enemies, physics, etc. here
    # --- Draw ---

    # Draw game objects here

    # Update display
    pygame.display.flip()

    # Limit FPS
    clock.tick(FPS)

# Quit
pygame.quit()
sys.exit()