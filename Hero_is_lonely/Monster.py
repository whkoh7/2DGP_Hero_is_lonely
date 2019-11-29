from plistlib import Data
from pico2d import *


class Monster_Class:
    image = None

    def __init__(self):
        self.x, self.y = 1080, 100
        if Monster_Class.image is None:
            Monster_Class.image = load_image('img/Ork_Monster.png')
        self.frame = 0
        self.velocity = 0
        self.frame = 0
        self.HP = 100
        self.ATK = 50
        self.DEF = 30
        self.Text = load_font('ALGER.TTF', 30)
        self.tick=0
        pass

    def add_event(self, event):
        pass

    def update(self):
        self.tick+=1
        if self.tick>100:
            self.frame = (self.frame + 1) % 2
            self.tick=0
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 60 + 8, 0, 60, 64, self.x, 800 - self.y)
        self.Text.draw(self.x - 50, 800 - self.y - 50, 'HP = %d' % self.HP, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 90, 'ATK = %d' % self.ATK, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 130, 'DEF = %d' % self.DEF, (255, 255, 255))
        pass
