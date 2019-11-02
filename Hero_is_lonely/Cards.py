from plistlib import Data

from Hero import Hero_Class
from Monster import Monster_Class
from pico2d import *


class Card:
    image = None

    def __init__(self):
        self.image = load_image('img/Card_Sample_Small.png')
        self.x, self.y = 200, 200
        self.clicked = False
        self.Available = False  # 덱에 들어가있는지
        self.exposed = False  # 핸드에 있는지
        # self.H_HP, self.H_ATK, self.H_DEF, self.M_HP, self.M_ATK, self.M_DEF = 0, 0, 0, 0, 0, 0

    def update(self):
        pass

    def click(self):
        self.image = load_image('img/Card_Sample_Big.png')
        self.clicked = True

    def Click_Up(self):
        self.image = load_image('img/Card_Sample_Small.png')
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
