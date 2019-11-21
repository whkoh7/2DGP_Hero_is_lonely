from plistlib import Data
from pico2d import *


class Mouse():
    def __init__(self):
        self.x, self.y = 0, 0
        self.Down=False
        self.Up=True

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def update(self):
        pass

    def draw(self):
        draw_rectangle(*self.get_bb())
