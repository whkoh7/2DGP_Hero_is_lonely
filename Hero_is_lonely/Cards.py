from plistlib import Data

from pico2d import *


class Card:
    image = None

    def __init__(self):
        self.image = load_image('Card_Sample_Small.png')
        self.x, self.y = 200, 200
        self.clicked = False

    def update(self):
        pass

    def click(self):
        self.image = load_image('Card_Sample_Big.png')
        self.clicked = True

    def Click_Up(self):
        self.image = load_image('Card_Sample_Small.png')
        self.clicked = False

    def draw(self):
        self.image.draw(self.x, self.y)
