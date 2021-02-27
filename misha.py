import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x_dest = 0
        self.y_dest = 0
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_S) and self.y == self.y_dest:
            self.y_dest += 10
        if pyxel.btnp(pyxel.KEY_W) and self.y == self.y_dest:
            self.y_dest -= 10
        if pyxel.btnp(pyxel.KEY_D) and self.x == self.x_dest:
            self.x_dest += 10
        if pyxel.btnp(pyxel.KEY_A) and self.x == self.x_dest:
            self.x_dest -= 10

        if self.y_dest != self.y:
            self.y += 1 if self.y_dest > self.y else -1
        if self.x_dest != self.x:
            self.x += 1 if self.x_dest > self.x else -1

    def draw(self):
        pyxel.cls(pyxel.COLOR_LIGHTBLUE)
        pyxel.rect(self.x, self.y, 10, 10, pyxel.COLOR_LIME)

App()
