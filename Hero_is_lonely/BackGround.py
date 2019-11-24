from plistlib import Data
from pico2d import *


class BackGround_Class:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('img/Background_Sample.jpg')
        self.frame = 0
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(100, 0, 1280, 800, 640, 400)