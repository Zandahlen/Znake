import logging
import pygame
import sys

#from controller import Controller
from player1 import Player1
from player2 import Player2
from fruit import Fruit
from indicator import Indicator

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
Survival = 0
SINGLEPLAYER = 1
MULTIPLAYER = 2


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
        self.Player2 = Player2(self.screen)
        self.Fruit = Fruit(self.screen)
        self.Indicator = Indicator(self.screen)

        # Initialize game state
        #self.game_state = STATE_RUNNING
        self.game_state = STATE_PREGAME


        self.font2 = pygame.font.SysFont("monospace", 10)
        self.font3 = pygame.font.SysFont("monospace", 15)
        self.font4 = pygame.font.SysFont("monospace", 20)
        self.font5 = pygame.font.SysFont("monospace", scale)
        self.font6 = pygame.font.SysFont("monospace", 30)

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
                        self.gamemode = self.Indicator.choice
                        self.game_state = STATE_RUNNING

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                        if self.Indicator.choice < 3:
                            self.Indicator.choice += 1
                        else:
                            self.Indicator.choice = 0

                        self.Indicator.tap()

                    if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                        if self.Indicator.choice != 0:
                            self.Indicator.choice -= 1
                        else:
                            self.Indicator.choice = 3

                        self.Indicator.tap()


                if self.game_state == STATE_RUNNING:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        self.game_state = STATE_PAUSED

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

                        # remove #
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                            #test av features
                            self.Player1.extend()
                            #self.Player1.lost = True
                            #self.Player2.lost = True
                            #self.Player1.size = self.Player1.size / 2

                    if self.gamemode == MULTIPLAYER:
                        if self.Player2.timeout == 0:
                            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP4 and self.Player2.direction != 3:
                                self.Player2.direction = 1
                                self.Player2.timeout = 1

                            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP8 and self.Player2.direction != 0:
                                self.Player2.direction = 2
                                self.Player2.timeout = 1

                            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP6 and self.Player2.direction != 1:
                                self.Player2.direction = 3
                                self.Player2.timeout = 1

                            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP5 and self.Player2.direction != 2:
                                self.Player2.direction = 0
                                self.Player2.timeout = 1


                if self.game_state == STATE_PAUSED:
                    if event.type == pygame.KEYDOWN and event.key != pygame.K_p:
                        self.game_state = STATE_RUNNING

                if self.game_state == STATE_GAMEOVER:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.Player1.reset()
                        if self.gamemode == MULTIPLAYER:
                            self.Player2.reset()
                        self.game_state = STATE_MENU

            # Manage game_state
            if self.game_state == STATE_PREGAME:
                self.screen.fill(COLOR['dark_red'])

                title = self.font5.render("PRESS ANY KEY TO CONTINUE", 1, COLOR['red'])

                w = title.get_width()
                h = title.get_height()

                #surface = pygame.Surface((lblpg.get_width() + 4, lblpg.get_height()))
                surface = pygame.Surface((w, h))
                surface.fill(COLOR['black'])
                self.screen.blit(surface, ((SCREEN_SIZE[0] - w) / 2, SCREEN_SIZE[1]/ 2 - h ))
                #pygame.draw.polygon(surface, COLOR['black'], ((w, 0), (0, 0), (0, h), (w, h)), 0)
                #self.screen.blit(surface, (surface.get_width / 2, surface.get_height / 2)

                self.screen.blit(title, (SCREEN_SIZE[0]/2 - w /2, SCREEN_SIZE[1]/2 - h ))


            if self.game_state == STATE_MENU:
                self.screen.fill(COLOR['black'])

                menu = self.font5.render("CHOOSE A GAMEMODE THEN", 1, (255,0,255))
                press = self.font6.render("PRESS ENTER TO PLAY!", 1, (255,0,255))
                survival = self.font5.render("Survival", 1, (0,0,250))
                singleplayer = self.font5.render("Singleplayer", 1, (0,0,255))
                multiplayer = self.font5.render("Multiplayer", 1, (0,0,255))

                w = menu.get_width()
                h = menu.get_height()

                surface = pygame.Surface((w, h))
                surface.fill(COLOR['yellow'])
                self.screen.blit(surface, ((SCREEN_SIZE[0] - w) / 2, SCREEN_SIZE[1]/ 2 + 2 * 32 ))
                self.screen.blit(surface, ((SCREEN_SIZE[0] - w) / 2, SCREEN_SIZE[1]/ 2 + 3 * 32 ))
                self.screen.blit(surface, ((SCREEN_SIZE[0] - w) / 2, SCREEN_SIZE[1]/ 2 + 4 * 32 ))

                self.screen.blit(survival, ((SCREEN_SIZE[0] - w) / 2, SCREEN_SIZE[1]/ 2 + 2 * 32))
                self.screen.blit(singleplayer, ((SCREEN_SIZE[0] - w) / 2, SCREEN_SIZE[1]/ 2 + 3 * 32))
                self.screen.blit(multiplayer, ((SCREEN_SIZE[0] - w) / 2, SCREEN_SIZE[1]/ 2 + 4 * 32))

                self.screen.blit(menu, (SCREEN_SIZE[0]/2 - w/2, SCREEN_SIZE[1]/2 - 2* h))
                self.screen.blit(press, (SCREEN_SIZE[0]/2 - press.get_width()/2, SCREEN_SIZE[1]/2 - press.get_height()))

                self.Indicator.x = (SCREEN_SIZE[0] - w )/ 2 - scale
                self.Indicator.draw()


            if self.game_state == STATE_RUNNING:
                self.screen.fill(COLOR['black'])

                self.Player1.draw()
                self.Player1.tick()

                if self.gamemode == MULTIPLAYER:
                    self.Player2.draw()
                    self.Player2.tick()

                self.Fruit.draw()
                self.Fruit.tick()

                if self.Player1.lost:
                    self.game_state = STATE_GAMEOVER

                if self.Player2.lost:
                    self.game_state = STATE_GAMEOVER

                if self.Player1.x == self.Fruit.x and self.Player1.y == self.Fruit.y:
                    self.Player1.extend()
                    self.Fruit.reset()

                #Prevents fruitspawns inside tail
                one_run = len(self.Player1.xlist) - 1
                while one_run > 0:
                    if self.Player1.xlist[one_run] == self.Fruit.x and self.Player1.ylist[one_run] == self.Fruit.y:
                        #logger.debug('replaced (1)')
                        self.Fruit.reset()

                    one_run -= 1

                if self.gamemode == MULTIPLAYER:
                    if self.Player2.x == self.Fruit.x and self.Player2.y == self.Fruit.y:
                        self.Player2.extend()
                        self.Fruit.reset()

                    #Prevents fruitspawns inside tail
                    two_run = len(self.Player2.xlist) - 1
                    while two_run > 0:
                        if self.Player2.xlist[two_run] == self.Fruit.x and self.Player2.ylist[two_run] == self.Fruit.y:
                            #logger.debug('replaced (2)')
                            self.Fruit.reset()

                        two_run -= 1

                    #collision manager
                    run1 = len(self.Player1.xlist) - 1
                    while run1 >= 0:
                        if self.Player1.xlist[run1] == self.Player2.x and self.Player1.ylist[run1] == self.Player2.y:
                            self.Player1.lost = True

                        run1 -= 1

                    run2 = len(self.Player2.xlist) - 1
                    while run2 >= 0:
                        if self.Player2.xlist[run2] == self.Player1.x and self.Player2.ylist[run2] == self.Player1.y:
                            self.Player2.lost = True

                        run2 -= 1

                    if self.Player1.x == self.Player2.x and self.Player1.y == self.Player2.y:
                        self.Player1.lost = True
                        self.Player2.lost = True


            if self.game_state == STATE_PAUSED:
                Paused = self.font3.render("Game paused!", 1, (0,255,255))
                Continue = self.font3.render("Press to Continue", 1, (0,255,255))
                self.screen.blit(Paused, (100, 100))
                self.screen.blit(Continue, (100, 125))

            if self.game_state == STATE_GAMEOVER:
                #self.screen.fill(COLOR['black'])
                gameoverlabel = 'GAME OVER!'
                if self.gamemode == MULTIPLAYER:
                    if self.Player1.lost and self.Player2.lost:
                        gameoverlabel = 'IT\'S A TIE!'
                    else:
                        if self.Player1.lost:
                            gameoverlabel = 'PLAYER 2 WINS!'
                        else:
                            if self.Player2.lost:
                                gameoverlabel = 'PLAYER 1 WINS!'


                over = self.font5.render(gameoverlabel, 1, (190,2,15))
                press = self.font4.render("PRESS ENTER TO CONTINUE!", 1, (190,255,255))
                self.screen.blit(over, (SCREEN_SIZE[0]/2 - over.get_width()/2, SCREEN_SIZE[1]/2 - over.get_height()))
                self.screen.blit(press, (SCREEN_SIZE[0]/2 - press.get_width()/2, SCREEN_SIZE[1]/2 + over.get_height()))


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
