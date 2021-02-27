import pyxel


class cRect:
    def __init__(self, x, y, w, h, col=0):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.vel = (0, 0)
        self.col = col
    
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.col)
    
    def collision(self, other):
        return self.x < other.x + other.w and \
               self.x + self.w > other.x and \
               self.y < other.y + other.h and \
               self.y + self.h > other.y
    
    def update(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
    
    def set_pos(self, x, y):
        self.x = x
        self.y = y


class cPlatform(cRect):
    def __init(self, x, y, w, h, col):
        super().__init__(x, y, w, h, col)
        self.active = True
    
    def checkcolls(self, player):
        if self.collision(player) and self.active:
            if player.falling:
                self.active = False
                return True
    
    def draw(self):
        if self.active:
            super().draw()


class Coin:
    def __init__(self, x, y, r, col=0):
        self.x, self.y = x, y
        self.r = r
        self.col = col
    
    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.col)
    
    def collision(self, center, r):
        if ((self.x - center.x) ** 2 + (self.y - center.y) ** 2) < self.r + r:
            return True
        return False
