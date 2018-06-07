from values import *

class Fruit():
    def __init__(self, screen):
        self.screen = screen
        self.xscaled = SCREEN_SIZE[0] / scale
        self.yscaled = SCREEN_SIZE[1] / scale
        self.reset()
        #self.x2 =
        #self.y2 =

    def reset(self):
        self.x = random.randint(2, self.xscaled) * scale - scale
        self.y = random.randint(2, self.yscaled) * scale - scale
        self.check()
        #add exception somehow??

    def tick(self):
        pass
        #self.reset()
        #COLOR['fuel'] = ((self.clock_tick * 20 ), 0, 0)

    def draw(self):
        fruit = pygame.Surface((scale - scale / 4, scale - scale / 4))
        fruit.fill(COLOR['green'])
        #pygame.draw.circle(fruit, COLOR['green'], [10, 10], 5, 5)
        #pygame.draw.circle(fruit, COLOR['green'], [10, 10], 10, 1)
        #pygame.draw.polygon(fuelP, COLOR['fuel'], ((9, 9), (9, 9), (9, 9)), 0)
        w = fruit.get_width() / 2
        h = fruit.get_height() / 2
        #pygame.draw.circle(fruit, COLOR['green'], [10, 10], 5, 1)
        pygame.draw.rect(fruit, COLOR['vibrant_green'], (w, 1, w, h), 0)
        self.screen.blit(fruit, (self.x - w, self.y - h))

    def check(self):
        pass
