from plistlib import Data
from pico2d import *


class Card:
    image = None

    def __init__(self):
        self.image = load_image('img/Card_Sample_Small.png')
        self.x, self.y = 200, 200
        self.clicked = False

    def get_bb(self):
        return self.x-100,self.y-140,self.x+100,self.y+140

    def update(self):
        pass

    def click(self):
        if self.clicked==False:
            self.y+=50
            self.clicked = True

    def click_up(self):
        if self.clicked:
            self.y-=50
            self.clicked = False

    def del_card(self):
        self.x=-1000
        self.y=-1000

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

