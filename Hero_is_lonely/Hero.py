from plistlib import Data
from pico2d import *


class Hero_Class:
    image = None
    hit_image = None

    def __init__(self):
        self.x, self.y = 200, 200
        if Hero_Class.image is None:
            Hero_Class.image = load_image('img/Hero_Sprite.png')
        if Hero_Class.hit_image is None:
            Hero_Class.hit_image = load_image('img/hit_effect.png')
        self.frame = 0
        self.HP = 100
        self.ATK = 30
        self.DEF = 30
        self.Text = load_font('ALGER.TTF', 30)
        self.tick = 0
        self.hit = False
        self.buf = False
        self.velocity = 0
        self.y_move = 0
        pass

    def add_event(self, event):
        pass

    def update(self):
        if self.hit is True:
            self.x += self.velocity
            if self.x < 150:
                self.velocity = 1
            if self.x >= 200 and self.velocity is 1:
                self.x, self.velocity = 200, 0
                self.hit = False

        if self.buf is True:
            self.y -= self.y_move
            if self.y < 150:
                self.y_move = -1
            if self.y >= 200 and self.y_move is -1:
                self.y, self.y_move = 200, 0
                self.buf = False

        self.tick += 1
        if self.tick > 100:
            self.frame = (self.frame + 1) % 2
            self.tick = 0
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 30 + 8, 170, 30, 55, self.x, 800 - self.y)
        # if self.hit is True:
        #   self.hit_image.clip_draw(self.frame * 80,0,80,90,self.x,800 - self.y)
        self.Text.draw(self.x - 50, 800 - self.y - 70, 'HP = %d' % self.HP, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 110, 'ATK = %d' % self.ATK, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 150, 'DEF = %d' % self.DEF, (255, 255, 255))
        pass

    def handle_event(self, event):
        pass
