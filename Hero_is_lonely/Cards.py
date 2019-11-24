from plistlib import Data

from Hero import Hero_Class
from Monster import Monster_Class
from pico2d import *
import main_state

card_size_x, card_size_y = 190, 250


class Card:
    image = None

    def __init__(self):
        if Card.image == None:
            Card.image = load_image('img/Card.Sample_Small_3.png')
        self.x, self.y = 150, 200
        self.clicked = False
        self.Available = False  # 덱에 들어가있는지
        self.exposed = False  # 핸드에 있는지
        self.Text = load_font('ALGER.TTF', 20)
        self.H_HP, self.H_ATK, self.H_DEF, self.M_HP, self.M_ATK, self.M_DEF, self.C_NUM = \
            0, 0, 0, -20, 0, 0, 1

    def get_bb(self):
        return self.x - card_size_x / 2, self.y - card_size_y / 2, self.x + card_size_x / 2, self.y + card_size_y / 2

    def update(self):
        pass

    def click(self):
        if not self.clicked:
            self.y += 50
            self.clicked = True

    def click_up(self):
        if self.clicked:
            self.y -= 50
            self.clicked = False

    def Card_In_Hand(self):
        pass

    def Card_Input(self):
        pass

    def del_card(self):
        self.x = -1000
        self.y = -1000
        hero = main_state.get_hero()
        monster = main_state.get_monster()
        hero.HP += self.H_HP
        hero.ATK += self.H_ATK
        hero.DEF += self.H_DEF
        monster.HP -= hero.ATK * self.C_NUM
        monster.ATK += self.M_ATK
        monster.DEF += self.M_DEF

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())
        self.Text.draw(self.x - 100, self.y + 140, '%.1f' % self.H_HP, (255, 255, 255))
        self.Text.draw(self.x - 70, self.y + 140, '%.1f' % self.H_ATK, (255, 255, 255))
        self.Text.draw(self.x - 40, self.y + 140, '%.1f' % self.H_DEF, (255, 255, 255))
        self.Text.draw(self.x - 10, self.y + 140, '%.1f' % self.M_HP, (255, 255, 255))
        self.Text.draw(self.x + 20, self.y + 140, '%.1f' % self.M_ATK, (255, 255, 255))
        self.Text.draw(self.x + 50, self.y + 140, '%.1f' % self.M_DEF, (255, 255, 255))
        self.Text.draw(self.x + 80, self.y + 140, '%.1f' % self.C_NUM, (255, 255, 255))
