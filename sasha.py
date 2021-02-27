import pyxel
from cRect import cRect
from map import inf_rect

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

        self.player = cRect(self.x, self.y, 10, 10, pyxel.COLOR_LIME)

        pyxel.run(self.update, self.draw_level)

    def update(self):
        if pyxel.btnp(pyxel.KEY_S):
            self.y_dest += 10
        if pyxel.btnp(pyxel.KEY_W):
            self.y_dest -= 10
        if pyxel.btnp(pyxel.KEY_D) and self.x == self.x_dest:
            self.x_dest += 10
        if pyxel.btnp(pyxel.KEY_A) and self.x == self.x_dest:
            self.x_dest -= 10

        if self.y_dest != self.y:
            self.y += 1 if self.y_dest > self.y else -1
            if self.y < 0:
                self.y = 0
            if self.y > 120 - self.height:
                self.y = 120 - self.height
        if self.x_dest != self.x:
            self.x += 1 if self.x_dest > self.x else -1
            if self.x < 0:
                self.x = 0
            if self.x > 160 - self.width:
                self.x = 160 - self.width

        if self.y_dest == self.y and self.y_dest != 120 - self.height: #and self.y >= 160 - self.height:
            self.y_dest = 120 - self.height

        self.player.set_pos(self.x, self.y)

    def draw_player(self):
        pyxel.cls(pyxel.COLOR_LIGHTBLUE)
        self.player.draw()
    
    def draw_level(self):
        for i in inf_rect:
            pyxel.rect(i[1], i[0], i[2], i[3], 11)
        

App()
