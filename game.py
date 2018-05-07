import logging
import pygame
import sys

# Values
FPS = 60
SCREEN_SIZE = (800,600)
CAPTION = 'Znake'

COLOR = {'playerOne': pygame.Color('#7799FF')
}

FONT = {'pregame1': pygame.font.SysFont("monospace", 40)
}

STATE_PREGAME = 1
STATE_MENU = 2
STATE_RUNNING = 3
STATE_PAUSED = 4
STATE_GAMEOVER = 5

class Controller():
    """Game controller"""

    def __init__(self):
        """Initialize game controller."""
        pygame.mixer.quit()
        self.fps = FPS

        pygame.init()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(CAPTION)

        # Initialize game state
        self.game_state = STATE_PREGAME

    def run(self):
        """Main game loop"""
        while True:
            # Manage event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # ALT + F4 or icon in upper right corner.
                    self.quit()

            # Manage game_state
            if self.game_state == STATE_PREGAME:

            if self.game_state == STATE_MENU:

            if self.game_state == STATE_RUNNING:

            if self.game_state == STATE_PAUSED:

            if self.game_state == STATE_GAMEOVER:


    def quit(self):
        #logging.info('Shutting down...')
        pygame.quit()
        sys.exit()

class Player1():
    def __init__(self, screen):
        self.screen = screen
        self.reset()

    def reset(self):
        pass

    def draw(self):
        pass

    def tick(self):
        pass


if __name__ == "__main__":
    logger.info('Starting...')
    c = Controller()
    c.run()
