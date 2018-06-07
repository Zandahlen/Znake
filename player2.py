from values import *

class Player2():
    def __init__(self, screen):
        self.screen = screen
        self.reset()

    def reset(self):
        self.lost = False
        self.x = SCREEN_SIZE[0] / 2 - scale * 2
        self.y = SCREEN_SIZE[1] / 2 - scale * 2
        self.direction = 0
        self.timeout = 0
        self.origintime = 10
        self.size = scale
        self.time = self.origintime
        self.xlist = [self.x]
        self.ylist = [self.y]

    def draw(self):
        head = pygame.Surface((self.size, self.size))
        head.fill(COLOR['player2'])
        w = head.get_width() / 2
        h = head.get_height() / 2

        tail = pygame.Surface((self.size, self.size))
        tail1 = pygame.Surface((self.size, self.size))
        tail2 = pygame.Surface((self.size, self.size))
        tail.fill(COLOR['player2tail'])
        tail1.fill(COLOR['player2tail'])
        tail2.fill(COLOR['player2tail'])
        pygame.draw.line(tail1, COLOR['yellow'], (self.size / 2, 0), (self.size / 2, self.size-1), 4)
        pygame.draw.line(tail2, COLOR['yellow'], (self.size-1, self.size / 2), (0, self.size / 2), 4)
        tailw = tail.get_width() / 2
        tailh = tail.get_height() / 2
        run = len(self.xlist) - 1
        while run >= 0:
            if run > 0:
                if self.xlist[run] == self.xlist[run-1]:
                    self.screen.blit(tail1, ( self.xlist[run] - tailw, self.ylist[run] - tailh))
                else:
                    self.screen.blit(tail2, ( self.xlist[run] - tailw, self.ylist[run] - tailh))
            else:
                if self.direction == 0 or self.direction == 2:
                    self.screen.blit(tail1, ( self.xlist[run] - tailw, self.ylist[run] - tailh))
                else:
                    self.screen.blit(tail2, ( self.xlist[run] - tailw, self.ylist[run] - tailh))

            run -= 1

        self.screen.blit(head, ( self.x - w, self.y - h))

    def tick(self):
        #reduces how often thing should happend for this player right now
        if self.time > 1:
            self.time -= 1
        else:
            self.time = self.origintime
            #reduces timeout
            if self.timeout > 0:
                self.timeout -= 1

            #out of window places you elsewhere
            if self.x < 0:
                self.x = SCREEN_SIZE[0]

            if self.x > SCREEN_SIZE[0]:
                self.x = 0

            if self.y < 0:
                self.y = SCREEN_SIZE[1]

            if self.y > SCREEN_SIZE[1]:
                self.y = 0

            self.collisionManager()

            #changes position of tailparts
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

            #changes position of head
            self.x = self.x + (abs(abs(1 - self.direction) + 1) - 2) * self.size
            self.y = self.y + (abs(self.direction - 2) - 1) * self.size

    def extend(self):
        #adds one to lists
        self.xlist[len(self.xlist):] = [self.xlist[len(self.xlist) - 1]]
        self.ylist[len(self.ylist):] = [self.ylist[len(self.ylist) - 1]]

    def collisionManager(self):
        run = len(self.xlist) - 1
        while run > 0:
#            if run != 0:
            if self.xlist[run] == self.x and self.ylist[run] == self.y:
                self.lost = True

            run -= 1
