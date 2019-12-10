from plistlib import Data
from pico2d import *
from random import *
import main_state


class Monster_Class:
    image = None

    def __init__(self):
        self.x, self.y = 1080, 200
        if Monster_Class.image is None:
            Monster_Class.image = load_image('img/Ork_Monster.png')
        self.frame = 0
        self.velocity = 0
        self.HP = 300
        self.ATK = 50
        self.DEF = 30
        self.Text = load_font('ALGER.TTF', 30)
        self.tick = 0
        self.hit = False
        self.buf = False
        pass

    def add_event(self, event):
        pass

    def monster_act(self):
        hero = main_state.get_hero()
        act = randint(0, 4)
        if act is 0:
            self.HP += 50
            self.buf = True
        elif act is 1:
            if hero.DEF > self.ATK * 2 :
                hero.hit = True
                hero.velocity = -1
                pass
            hero.HP -= (hero.DEF - self.ATK * 2)
            hero.hit = True
            hero.velocity = -1
        elif act is 2:
            self.DEF += 20
            self.buf = True
        elif act is 3:
            self.ATK += 10
            self.buf = True
        pass

    def update(self):
        if self.hit is True:
            self.x += self.velocity
            if self.x > 1130:
                self.velocity = -1
            if self.x <= 1080 and self.velocity is -1:
                self.x, self.velocity = 1080, 0
                self.hit = False
                self.monster_act()

        if self.buf is True:
            self.y -= self.velocity
            if self.y <150:
                self.velocity = -1
            if self.y >= 200 and self.velocity is -1:
                self.y, self.velocity = 200,0
                self.buf = False
        self.tick += 1
        if self.tick > 100:
            self.frame = (self.frame + 1) % 2
            self.tick = 0


    def draw(self):
        self.image.clip_draw(self.frame * 60 + 8, 0, 60, 64, self.x, 800 - self.y)
        self.Text.draw(self.x - 50, 800 - self.y - 70, 'HP = %d' % self.HP, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 110, 'ATK = %d' % self.ATK, (255, 255, 255))
        self.Text.draw(self.x - 50, 800 - self.y - 150, 'DEF = %d' % self.DEF, (255, 255, 255))
        pass
