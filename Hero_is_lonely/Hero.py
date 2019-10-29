from plistlib import Data
from pico2d import *


class Hero_Class:
    image = None

    def __init__(self):
        self.x, self.y = 200, 100
        if Hero_Class.image is None:
            Hero_Class.image = load_image('Hero_Sprite.png')
        self.frame = 0
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        pass

    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += 0
        delay(0.1)
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 30+8, 225, 30, 55, self.x, 800-self.y)
        pass

    def handle_event(self, event):
        pass
