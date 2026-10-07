import pygame
import sys
import os
import time

import Bird
import Pipe

# TODO
#   collision pygame.mask()
#   make bird and pipe seperate files
#   init random starting weights



# UI settings
WIDTH = 1000
HEIGHT = 700

# Game settings
POLE_WIDTH = 300
GAP_BETWEEN_POLES = 150
NEXT_POLE_DISTANCE = 120
BIRD_SPAWN_Y = 150
PIPE_SPEED = 4
STOP = 800
FPS = 30
AI_MODE = False

## imgs
backround_img = pygame.image.load(os.path.join("Images/flappy_bird_backround2.png"))
backround_img = pygame.transform.scale(backround_img, (WIDTH, HEIGHT))


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
    return False


def generate_pipes(pipes_array):
    for p in pipes_array:
        p.draw_pipe(SCREEN=SCREEN)
        if p.x < -120:
            pipes.remove(p)


# Initialize Pygame
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock for controlling FPS
clock = pygame.time.Clock()

running = True
frame_count = 0
pipes = []
birds = [Bird.Bird()]
newPole = Pipe.Pipe()
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
    if keys[pygame.K_b]:
        time.sleep(30)

    # --- Update ---
    SCREEN.blit(backround_img, (0, 0))

    if should_spawn_pipe(frame_count):          #spawn pipes
        pipes.append(Pipe.Pipe())
    generate_pipes(pipes)

    for bird in birds:                          # render birds
        bird.draw_bird(SCREEN=SCREEN)
        if not AI_MODE and bird.collision():            # will usally short circut
            running = end_game()
        elif AI_MODE or True:
            nextPipe = Pipe.get_next_pipe(pipe_list=pipes)     # fix later
            pygame.draw.line(SCREEN, (255, 0, 0), (nextPipe.get_x(), nextPipe.get_top()), (nextPipe.get_x() + 80, nextPipe.get_top()), 1)
            pygame.draw.line(SCREEN, (255, 0, 0), (nextPipe.get_x(), nextPipe.get_bottom()), (nextPipe.get_x() + 80, nextPipe.get_bottom()), 1)
            pygame.draw.line(SCREEN, (255, 0, 0), (nextPipe.get_x(), nextPipe.get_top() - 50 ), (nextPipe.get_x(), nextPipe.get_bottom() + 50), 1)
            bird.flap_decision(nextPipe.get_top(), nextPipe.get_bottom(), nextPipe.get_x())

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
print(" \n \n  GAME OVER RESET \n \n \n")
pygame.quit()
sys.exit()
