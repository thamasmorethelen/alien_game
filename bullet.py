import pygame
from pygame.sprite import Sprite

#class to manage bullets the spaceship shoots.
class Bullet(Sprite):

    def __init__(self, ai_game):
        # create bullet at ship's location
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet location as float
        self.y = float(self.rect.y)

    def update(self):
        # moves bullets
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # draws bullet
        pygame.draw.rect(self.screen, self.color, self.rect)
