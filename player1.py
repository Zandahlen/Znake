from values import *

class Player1():
    def __init__(self, screen):
#    def __init__(self, screen, pos, color):
        self.screen = screen
        self.reset()

    def reset(self):
        self.lost = False
        self.x = SCREEN_SIZE[0] / 2 + scale * 2
        self.y = SCREEN_SIZE[1] / 2 + scale * 2
        self.direction = 2
        self.timeout = 0
        self.origintime = 14
        self.size = scale
        self.time = self.origintime
        self.xlist = [self.x]
        self.ylist = [self.y]

    def draw(self):
        head = pygame.Surface((self.size, self.size))
        head.fill(COLOR['yellow'])
        w = head.get_width() / 2
        h = head.get_height() / 2

        tail = pygame.Surface((self.size, self.size))
        tailf = pygame.Surface((self.size, self.size))
        #tail2 = pygame.Surface((self.size, self.size))
        tail.fill(COLOR['green'])
        tailf.fill(COLOR['green'])
        #tail2.fill(COLOR['green'])
        pygame.draw.polygon(tail, COLOR['yellow'], ((0, 0), (self.size/4-1, self.size/2 -1), (0, self.size-1), (self.size-1, self.size/2 -1)), 0)
        #pygame.draw.line(tail, COLOR['black'], (0, 0), (self.size-1, 0), 4)
        #pygame.draw.line(tail, COLOR['black'], (self.size-1, self.size-1), (0, self.size-1), 4)
        tail = pygame.transform.rotate(tail, 270)
        tailf = tail
        #tail0 = pygame.transform.rotate(tail, 0)
        tail0 = tail
        tail1 = pygame.transform.rotate(tail, 90)
        tail2 = pygame.transform.rotate(tail, 180)
        tail3 = pygame.transform.rotate(tail, 270)
        tailw = tail.get_width() / 2
        tailh = tail.get_height() / 2
        run = 0
        while run <= len(self.xlist) - 1:
            if run > 0:
                if self.xlist[run] == self.xlist[run-1]:
                    if self.ylist[run] > self.ylist[run-1]:
                        tail = tail2
                    else:
                        tail = tail0
                else:
                    if self.xlist[run] > self.xlist[run-1]:
                        tail = tail3
                    else:
                        tail = tail1

                self.screen.blit(tail, ( self.xlist[run] - tailw, self.ylist[run] - tailh))
            else:
                tailf = pygame.transform.rotate(tailf, self.direction * -90)
                self.screen.blit(tailf, ( self.xlist[run] - tailw, self.ylist[run] - tailh))

            run += 1

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
            for x in range(len(self.xlist) - 1, 0, -1):
                #doesn't renew when the len value changes??
                self.xlist[x] = self.xlist[x - 1]
                self.ylist[x] = self.ylist[x - 1]

            self.xlist[0] = self.x
            self.ylist[0] = self.y


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
            if self.xlist[run] == self.x and self.ylist[run] == self.y:
                self.lost = True

            run -= 1
