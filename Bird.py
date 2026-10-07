import pygame.image
import os

bird_img = pygame.image.load(os.path.join("Images/ChatGPT Image Sep 16, 2026, 06_55_27 PM.png"))
bird_img = pygame.transform.scale(bird_img, (70, 55))


class Bird():
    GRAVITY = -2.3
    FLAP_STRENGTH = 12
    MAX_SPEED = -15
    BIRD_SPAWN_Y = 150

    def __init__(self):
        self.y = 300
        self.velocity_y = 0

    def draw_bird(self, SCREEN):
        if self.velocity_y > self.MAX_SPEED:        # inceasing gravity
            self.velocity_y += self.GRAVITY
        self.y -= self.velocity_y           # in the frame
        SCREEN.blit(bird_img, (150, self.y))

    def flap(self):
        self.velocity_y = self.FLAP_STRENGTH + self.velocity_y / 5

    def flap_decision(self, top_pipe_VTD, bottom_pipe_VTD, pipe_HD):
        top_pipe_VTD = self.y - top_pipe_VTD
        bottom_pipe_VTD = self.y - bottom_pipe_VTD
        pipe_HD -= self.BIRD_SPAWN_Y - 70
        inputs = [top_pipe_VTD, bottom_pipe_VTD, pipe_HD, self.velocity_y]
        print(inputs[2])
        # print("topVTD,        bottomVTD,       HD,  B.velo")

    # Vertical distance from bird to top of next pipe gap.
    # Vertical distance from bird to bottom of next pipe gap.
    # Horizontal distance to next pipe.
    # Bird’s current vertical velocity.

    def collision(self):
        if self.y > 640 or self.y < -10:        # top / bottom collision
            return True
        else:
            pass

    def get_height(self):
        return self.y

    def get_velo(self):
        return self.velocity_y

