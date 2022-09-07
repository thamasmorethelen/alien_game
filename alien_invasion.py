import sys
import pygame

from settings import Settings
from ship import Ship

# class to manage overall behavior of the game
class AlienInvasion:

    def __init__(self):
        # Initiates the game and creates game resources
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        # method for main loop of game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraws the screen for each iteration of the loop.
            self.screen.fill(self.settings.bg_color)
            # Makes the most recently drawn screen visable
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
