from plistlib import Data
from pico2d import *

class BackGround_Class:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('Background_Sample.jpg')
        self.frame = 0
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.frame, 0, 800, 800, 400, 400)