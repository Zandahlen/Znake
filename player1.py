from values import *

class Player1():
    def __init__(self, screen):
        self.screen = screen
        self.reset()

    def reset(self):
        self.x = SCREEN_SIZE[0] / 2
        self.y = SCREEN_SIZE[1] / 2
        self.direction = 0
#        self.length = (0, 1)
        self.speed = 8
        self.timeout = 0
        self.size = 20
        self.origintime = 10
        self.time = self.origintime
        # self.x1 = self.x
        # self.y1 = self.y
        # self.x2 = self.x1
        # self.y2 = self.y1
        self.xlist = [self.x, self.x, self.x]
        self.ylist = [self.y, self.y, self.y]

    def draw(self):
        head = pygame.Surface((self.size, self.size))
        head.fill(COLOR['player1'])
        w = head.get_width() / 2
        h = head.get_height() / 2
        self.screen.blit(head, ( self.x - w, self.y - h))

        tail = pygame.Surface((self.size, self.size))
        tail.fill(COLOR['player1tail'])
        tailw = tail.get_width() / 2
        tailh = tail.get_height() / 2
        run = len(self.xlist) - 1
        while run >= 0:
            self.screen.blit(tail, ( self.xlist[run] - tailw, self.ylist[run] - tailh))
            run -= 1

    def tick(self):
        if self.time > 1:
            self.time -= 1
        else:
            self.time = self.origintime
            if self.timeout > 0:
                self.timeout -= 1

            run = len(self.xlist) - 1
            while run >= 0:
                if run != 0:
                    self.xlist[run] = self.xlist[run - 1]
                    self.ylist[run] = self.ylist[run - 1]
                    run -= 1
                else:
                    self.xlist[0] = self.x
                    self.ylist[0] = self.y
                    run -= 1


            self.x = self.x + (abs(abs(1 - self.direction) + 1) - 2) * self.size
            self.y = self.y + (abs(self.direction - 2) - 1) * self.size

    def extend(self):
        self.xlist[len(self.xlist):] = [self.x]
        self.ylist[len(self.ylist):] = [self.y]
