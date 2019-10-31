from plistlib import Data
from pico2d import *


class Monster_Class:
    image = None

    def __init__(self):
        self.x, self.y = 600, 100
        if Monster_Class.image is None:
            Monster_Class.image = load_image('Ork_Monster.png')
        self.frame = 0
        self.velocity = 0
        self.frame = 0
        self.hp = 100
        self.attack = 50
        self.defense = 30
        self.Text = load_font('ALGER.TTF', 30)
        pass

    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame + 1) % 2
        self.x += 0
        delay(0.1)
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 60 + 8, 0, 60, 64, self.x, 800 - self.y)
        self.Text.draw(self.x - 50, 800 - self.y - 50, 'HP = %d' % self.hp, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 90, 'ATTACK = %d' % self.attack, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 130, 'DEF = %d' % self.defense, (255, 255, 255))
        pass
