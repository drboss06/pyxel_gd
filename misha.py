import pyxel
from cRect import cRect, cPlatform


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

        self.platform = cPlatform(140, 60, 30, 10, pyxel.COLOR_PEACH)

        self.x_v = 0
        self.y_v = 0

        self.player = cRect(self.x, self.y, 10, 10, pyxel.COLOR_LIME)
        pyxel.load("assets/jump_game.pyxres")
        pyxel.playm(0, loop=True)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_W) and self.y_v == 0:
            self.y_v = -10
            pyxel.play(3, 3)
        if pyxel.btnp(pyxel.KEY_D):
            self.x_v += 2
        if pyxel.btnp(pyxel.KEY_A):
            self.x_v -= 2
        if pyxel.btnr(pyxel.KEY_D):
            self.x_v = 0
        if pyxel.btnr(pyxel.KEY_A):
            self.x_v = 0

        self.x += self.x_v
        if self.platform.collision(self.player):
            self.x = 0

        self.y += self.y_v
        if self.platform.collision(self.player):
            self.y = 150


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
        
        self.platform.draw()

App()
