import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_W):
            self.y += 10
        if pyxel.btnp(pyxel.KEY_S):
            self.y -= 10

    def draw(self):
        pyxel.cls(pyxel.COLOR_LIGHTBLUE)
        pyxel.rect(self.x, self.y, 10, 10, pyxel.COLOR_LIME)

App()
