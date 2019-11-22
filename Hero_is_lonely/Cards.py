from plistlib import Data

from Hero import Hero_Class
from Monster import Monster_Class
from pico2d import *


class Card:
    image = None

    def __init__(self):
        self.image = None
        self.x, self.y = 200, 200
        self.clicked = False
        self.Available = False  # 덱에 들어가있는지
        self.exposed = False  # 핸드에 있는지
        # self.H_HP, self.H_ATK, self.H_DEF, self.M_HP, self.M_ATK, self.M_DEF = 0, 0, 0, 0, 0, 0

    def get_bb(self):
        return self.x - 100, self.y - 140, self.x + 100, self.y + 140

    def update(self):
        pass

    def click(self):
        if self.clicked == False:
            self.y += 50
            self.clicked = True

    def click_up(self):
        if self.clicked:
            self.y -= 50
            self.clicked = False

    def Card_In_Hand(self):
        pass

    def Card_Input(self):
        pass

    def del_card(self):
        self.x = -1000
        self.y = -1000

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
