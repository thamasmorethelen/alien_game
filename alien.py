import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # class for the alien ship

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # load alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # alien start loaction
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's location
        self.x = float(self.rect.x)

