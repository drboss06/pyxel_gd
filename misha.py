import pyxel
from cRect import cRect


GRAVITY = 1


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.width = 10
        self.height = 10
        self.x_dest = 0
        self.y_dest = 120 - self.height
        self.x = 0
        self.y = self.y_dest

        self.x_v = 0
        self.y_v = 0

        self.player = cRect(self.x, self.y, 10, 10, pyxel.COLOR_LIME)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_W) and self.y_v == 0:
            self.y_v = -10
        if pyxel.btnp(pyxel.KEY_D):
            self.x_v += 2
        if pyxel.btnp(pyxel.KEY_A):
            self.x_v -= 2
        if pyxel.btnr(pyxel.KEY_D):
            self.x_v = 0
        if pyxel.btnr(pyxel.KEY_A):
            self.x_v = 0

        self.x += self.x_v
        self.y += self.y_v

        if self.y < 120 - self.height:
            self.y_v += GRAVITY

        if self.y == 120 - self.height and self.y_v > 0:
            self.y_v = 0
        
        if self.x > 160 - self.width:
            self.x = 160 - self.width

        if self.x < 0:
            self.x = 0

        self.player.set_pos(self.x, self.y)

    def draw(self):
        pyxel.cls(pyxel.COLOR_LIGHTBLUE)
        self.player.draw()
        

App()
