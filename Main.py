import random
import pygame
import sys
import os
import time

# TODO
#   collision pygame.mask() ?
#   getters for pipe location
#   getters for distance to pipe
#   figute out all imputs for the AI


# UI settings
WIDTH = 1000
HEIGHT = 700

# Game settings
POLE_WIDTH = 300
GAP_BETWEEN_POLES = 150
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
top_pipe_img = pygame.transform.scale(top_pipe_img, (POLE_WIDTH, 600))
bottom_pipe_img = pygame.image.load(os.path.join("Images/flappy_bird_bottom_pipe.png"))
bottom_pipe_img = pygame.transform.scale(bottom_pipe_img, (POLE_WIDTH, 600))


def should_spawn_pipe(count):
    if count % NEXT_POLE_DISTANCE == 0 or count == 0:
        return True
    else:
        return False


def end_game():
    font = pygame.font.Font(None, 100)
    text = font.render("GAME OVER", True, (220, 0, 0))  # ending game in player mode
    SCREEN.blit(text, (300, 300))
    pygame.display.flip()
    running = False
    time.sleep(2)


def generate_pipes(pipes_array):
    for p in pipes_array:
        p.draw_pipe()
        if p.x < -120:
            pipes.remove(p)


class Bird():
    GRAVITY = -2.3
    FLAP_STRENGTH = 12
    MAX_SPEED = -15

    def __init__(self):
        self.y = 300
        self.velocity_y = 0

    def draw_bird(self):
        if self.velocity_y > self.MAX_SPEED:        # inceasing gravity
            self.velocity_y += self.GRAVITY
        self.y -= self.velocity_y           # in the frame
        SCREEN.blit(bird_img, (150, self.y))

    def flap(self):
        self.velocity_y = self.FLAP_STRENGTH + self.velocity_y / 5

    def flap_decision(self, top_pipe_VTD, bottom_pipe_V, pipe_HD):
        top_pipe_VTD = self.y - top_pipe_VTD
        bottom_pipe_V = self.y - top_pipe_VTD
        inputs = [top_pipe_VTD, bottom_pipe_V, pipe_HD, self.velocity_y]
        print(inputs)

    # Vertical distance from bird to top of next pipe gap.
    # Vertical distance from bird to bottom of next pipe gap.
    # Horizontal distance to next pipe.
    # Bird’s current vertical velocity.

    def collision(self):
        if self.y > 640 or self.y < -10:        # top / bottom collision
            return True

    def get_height(self):
        return self.y

    def get_velo(self):
        return self.velocity_y


class Pipe():
    def __init__(self):
        self.pipe_bottom = random.randint(130, 600)
        self.pipe_top = self.pipe_bottom - GAP_BETWEEN_POLES
        self.x = 950

    def draw_pipe(self):
        SCREEN.blit(top_pipe_img, (self.x, self.pipe_top - 500))
        SCREEN.blit(bottom_pipe_img, (self.x, self.pipe_bottom))
        self.x -= PIPE_SPEED

    def get_bottom(self):
        return self.pipe_bottom

    def get_top(self):
        return self.pipe_top

    def get_x(self):
        return self.x

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
            end_game()
        elif AI_MODE or True:
            nextPipe = pipes[0]     # fix later
            bird.flap_decision(nextPipe.pipe_top, nextPipe.pipe_bottom, nextPipe.get_x() )

    # SCREEN.blit(bird_img, (150, 300))
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