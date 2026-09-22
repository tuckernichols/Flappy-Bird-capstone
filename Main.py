import random
import pygame
import sys
import os
import time
import math # fix gravity, collision pygame.mask() ?


# UI settings
WIDTH = 1000
HEIGHT = 700

# Game settings
GAP_BETWEEN_POLES = 140
NEXT_POLE_DISTANCE = 120
PIPE_SPEED = 4
STOP = 800
FPS = 30
AI_MODE = False

## imgs
backround_img = pygame.image.load(os.path.join("Images/flappy_bird_backround2.png"))
backround_img = pygame.transform.scale(backround_img, (WIDTH, HEIGHT))

bird_img = pygame.image.load(os.path.join("Images/ChatGPT Image Sep 16, 2026, 06_55_27 PM.png"))
bird_img = pygame.transform.scale(bird_img, (70, 55))

top_pipe_img = pygame.image.load(os.path.join("Images/flappy_bird_top_pipe.png"))
top_pipe_img = pygame.transform.scale(top_pipe_img, (300, 600))
bottom_pipe_img = pygame.image.load(os.path.join("Images/flappy_bird_bottom_pipe.png"))
bottom_pipe_img = pygame.transform.scale(bottom_pipe_img, (300, 600))


def should_spawn_pipe(count):
    if count % NEXT_POLE_DISTANCE == 0 or count == 0:
        return True
    else:
        return False


def generate_pipes(pipes_array):
    for p in pipes_array:
        p.draw_pipe()
        if p.x < -120:
            pipes.remove(p)


class Bird():
    GRAVITY = -2.2
    FLAP_STRENGTH = 13
    MAX_SPEED = -15

    def __init__(self):
        self.y = 300
        self.velocity_y = 0

    def draw_bird(self):
        if self.velocity_y > self.MAX_SPEED:
            self.velocity_y += self.GRAVITY
        self.y -= self.velocity_y
        SCREEN.blit(bird_img, (700, self.y))

    def flap(self):
        print("flap")
        self.velocity_y = self.FLAP_STRENGTH + self.velocity_y / 5

    def collision(self):
        return False


class Pipe():
    def __init__(self):
        self.pipe_bottom = random.randint(130, 600)
        self.pipe_top = self.pipe_bottom - GAP_BETWEEN_POLES
        self.x = 950

    def draw_pipe(self):
        SCREEN.blit(top_pipe_img, (self.x, self.pipe_top - 500))
        SCREEN.blit(bottom_pipe_img, (self.x, self.pipe_bottom))
        self.x -= PIPE_SPEED


# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock for controlling FPS
clock = pygame.time.Clock()

running = True
frame_count = 0
pipes = []
birds = [Bird()]
newPole = Pipe()
pipes.append(newPole)
pole_made = False

while running:
    frame_count += 1
    if frame_count > STOP:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        for bird in birds:
            bird.flap()

    # --- Update ---
    SCREEN.blit(backround_img, (0, 0))

    if should_spawn_pipe(frame_count):          #spawn pipes
        pipes.append(Pipe())
    generate_pipes(pipes)

    for bird in birds:                          # render birds
        bird.draw_bird()
        if not AI_MODE and bird.collision():            # will usally short circut
            font = pygame.font.Font(None, 100)
            text = font.render("GAME OVER", True, (220, 0, 0))   # ending game in player mode
            SCREEN.blit(text, (300, 300))
            running = False
            time.sleep(2)

    SCREEN.blit(bird_img, (150, 300))
    # SCREEN.blit(top_pipe_img, (500, -30))
    # SCREEN.blit(bottom_pipe_img, (500, 600))
    #
    # SCREEN.blit(top_pipe_img, (400, -500))
    # SCREEN.blit(bottom_pipe_img, (400, 130))

    # Update display
    pygame.display.flip()
    # Limit FPS
    clock.tick(FPS)

# Quit
pygame.quit()
sys.exit()