import sys
import pygame

# class to manage overall behavior of the game
class AlienInvasion:
    # Initiates the game and creates game resources
    pygame.init()

    self.screen = pygame.display.set_mode(1200, 800)
    pygame.display.set_caption("Alien Invasion")

    # method for main loop of game
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()