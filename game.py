import logging
import pygame
import sys

#from controller import Controller
from player1 import Player1

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

# Values
from values import *



#FONT = {'pregame1': pygame.font.SysFont("monospace", 40)}

#Gamestates
STATE_PREGAME = 1
STATE_MENU = 2
STATE_RUNNING = 3
STATE_PAUSED = 4
STATE_GAMEOVER = 5

#Gamemodes
CLASSIC = 0
SINGLE_PLAYER = 1
TWO_PLAYER = 2


class Controller():
    """Game controller"""

    def __init__(self):
        """Initialize game controller."""
        self.fps = FPS

        pygame.init()
        pygame.mixer.quit()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

        self.Player1 = Player1(self.screen)

        # Initialize game state
        #self.game_state = STATE_RUNNING
        self.game_state = STATE_PREGAME

        self.gamemode = CLASSIC

        self.font2 = pygame.font.SysFont("monospace", 25)
        self.font4 = pygame.font.SysFont("monospace", 20)

    def run(self):
        """Main game loop"""
        while True:
            # Manage event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # ALT + F4 or icon in upper right corner.
                    self.quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    # Escape key pressed.
                    self.quit()

                if self.game_state == STATE_PREGAME:
                    if event.type == pygame.KEYDOWN:
                        self.game_state = STATE_MENU

                if self.game_state == STATE_MENU:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.game_state = STATE_RUNNING

                if self.game_state == STATE_RUNNING:
                    if self.Player1.timeout == 0:
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_a and self.Player1.direction != 3:
                            self.Player1.direction = 1
                            self.Player1.timeout = 1

                        if event.type == pygame.KEYDOWN and event.key == pygame.K_w and self.Player1.direction != 0:
                            self.Player1.direction = 2
                            self.Player1.timeout = 1

                        if event.type == pygame.KEYDOWN and event.key == pygame.K_d and self.Player1.direction != 1:
                            self.Player1.direction = 3
                            self.Player1.timeout = 1

                        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and self.Player1.direction != 2:
                            self.Player1.direction = 0
                            self.Player1.timeout = 1

                        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                            #test av extend
                            self.Player1.extend()
                            self.Player1.timeout = 1


                    """
                    if event.type == pygame.KEYUP and event.key == pygame.K_w:
                    if event.type == pygame.KEYUP and event.key == pygame.K_d:
                    if event.type == pygame.KEYUP and event.key == pygame.K_a:
                    if event.type == pygame.KEYUP and event.key == pygame.K_s:
                    """

                if self.game_state == STATE_PAUSED:
                    pass

                if self.game_state == STATE_GAMEOVER:
                    pass

            # Manage game_state
            if self.game_state == STATE_PREGAME:
                self.screen.fill(COLOR['dark_red'])

                title = self.font2.render("PRESS ANY KEY TO CONTINUE", 1, COLOR['red'])

                w = title.get_width()
                h = title.get_height()

                #surface = pygame.Surface((lblpg.get_width() + 4, lblpg.get_height()))
                surface = pygame.Surface((w, h))
                surface.fill(COLOR['bg'])
                #pygame.draw.polygon(surface, COLOR['black'], ((w, 0), (0, 0), (0, h), (w, h)), 0)
                self.screen.blit(surface, ((SCREEN_SIZE[0] - w) / 2, SCREEN_SIZE[1]/ 2 - h ))
                #self.screen.blit(surface, (surface.get_width / 2, surface.get_height / 2)


                self.screen.blit(title, (SCREEN_SIZE[0]/2 - w /2, SCREEN_SIZE[1]/2 - h ))


            if self.game_state == STATE_MENU:
                self.screen.fill(COLOR['bg'])

                menu = self.font2.render("Welcome to the menu", 1, (0,255,255))
                press = self.font4.render("PRESS ENTER TO PLAY!", 1, (0,255,255))
                self.screen.blit(menu, (SCREEN_SIZE[0]/2 - menu.get_width()/2, SCREEN_SIZE[1]/2 - menu.get_height()))
                self.screen.blit(press, (SCREEN_SIZE[0]/2 - press.get_width()/2, SCREEN_SIZE[1]/2 + menu.get_height()))


            if self.game_state == STATE_RUNNING:
                self.screen.fill(COLOR['bg'])

                self.Player1.draw()

                self.Player1.tick()

            if self.game_state == STATE_PAUSED:
                pass

            if self.game_state == STATE_GAMEOVER:
                pass

            pygame.display.flip()

            self.clock.tick(self.fps)


    def quit(self):
        #logging.info('Shutting down...')
        pygame.quit()
        sys.exit()



if __name__ == "__main__":
    logger.info('Starting...')
    c = Controller()
    c.run()
