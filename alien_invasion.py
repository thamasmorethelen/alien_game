import sys
import pygame

from settings import Settings


# class to manage overall behavior of the game
class AlienInvasion:


    # Initiates the game and creates game resources
    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        

    # method for main loop of game
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #redraws the screen for each iteration of the loop.
            self.screen.fill(self.settings.bg_color)
            # Makes the most recently drawn screen visable
            pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
