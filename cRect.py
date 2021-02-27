import pyxel


class cRect:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h
    
    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h)
    
    def collision(self, other):
        return self.x < other.x + other.w and \
               self.x + self.w > other.x and \
               self.y < other.y + other.h and \
               self.y + self.h > other.y
