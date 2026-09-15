import pygame
import sys
import os

WIDTH = 1000
HEIGHT = 700

## imgs
backround_img = pygame.image.load(os.path.join("Images/flappy_bird_backround2.png"))
backround_img = pygame.transform.scale(backround_img, (WIDTH, HEIGHT))

# Initialize Pygame
pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock for controlling FPS
clock = pygame.time.Clock()
FPS = 30

running = True
count = 0
while running:
    count += 1
    if count > 200:
        running = False

    SCREEN.blit(backround_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    # --- Update ---
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