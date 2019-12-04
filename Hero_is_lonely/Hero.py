from plistlib import Data
from pico2d import *


class Hero_Class:
    image = None

    def __init__(self):
        self.x, self.y = 200, 200
        if Hero_Class.image is None:
            Hero_Class.image = load_image('img/Hero_Sprite.png')
        self.frame = 0
        self.HP = 100
        self.ATK = 50
        self.DEF = 30
        self.Text = load_font('ALGER.TTF', 30)
        self.tick = 0
        pass

    def add_event(self, event):
        pass

    def update(self):
        self.tick+=1
        if self.tick > 100:
            self.frame = (self.frame + 1) % 2
            self.tick = 0
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 30 + 8, 225, 30, 55, self.x, 800 - self.y)
        self.Text.draw(self.x - 50, 800 - self.y - 70, 'HP = %d' % self.HP, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 110, 'ATK = %d' % self.ATK, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 150, 'DEF = %d' % self.DEF, (255, 255, 255))
        pass

    def handle_event(self, event):
        pass