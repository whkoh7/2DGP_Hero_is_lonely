from plistlib import Data
from pico2d import *


class Hero_Class:
    image = None

    def __init__(self):
        self.x, self.y = 200, 100
        if Hero_Class.image is None:
            Hero_Class.image = load_image('img/Hero_Sprite.png')
        self.frame = 0
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.hp = 100
        self.attack = 50
        self.Text = load_font('ALGER.TTF', 30)
        self.defense = 30
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
        self.Text.draw(self.x - 50, 800 - self.y - 50, 'HP = %d' % self.hp, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 90, 'ATTACK = %d' % self.attack, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 130, 'DEF = %d' % self.defense, (255, 255, 255))
        pass

    def handle_event(self, event):
        pass
