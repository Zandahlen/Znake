from values import *

class Indicator():
    def __init__(self, screen):
        self.screen = screen
        self.reset()

    def reset(self):
        self.choice = 1
        self.x = SCREEN_SIZE[0] / 2
        self.tap()

    def draw(self):
        marker = pygame.Surface((scale, scale))
        w = marker.get_width
        h = marker.get_height
        pygame.draw.polygon(marker, COLOR['yellow'], ((0, 0), (scale / 4 -1, scale / 2 -1), (0, scale -1), (scale -1, scale/2 - 1)), 0)

        self.screen.blit(marker, ( self.x, self.y ))

    def tap(self):
        self.y = SCREEN_SIZE[1] / 2 + scale * 2 + scale * self.choice
