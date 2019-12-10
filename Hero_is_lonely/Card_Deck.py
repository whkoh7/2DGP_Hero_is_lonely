from pico2d import *
from Cards import Card
import main_state


# 카드 객체를 불러와서 각각 스탯과 이미지 로드해주는 기능
class Deck:
    def __init__(self):
        # card_num, H_HP, H_ATK, H_DEF, M_HP, M_ATK, M_DEF, C_NUM, activated 선언
        self.card_list = [0, 10, 0, 0, 0, 0, 0, 0, 0,
                          1, 0, 0, 10, 0, 0, 0, 0, 0,
                          2, 0, 15, 0, 0, 0, 0, 0, 0,
                          3, 0, 10, 0, 0, 0, 0, 0.6, 0,
                          4, 0, 15, 15, 0, 0, 0, 0.8, 0,
                          5, 0, 0, 0, 0, 0, 0, 1.5, 0,
                          6, 40, 0, 0, 0, 0, 0, 0, 0,
                          7, 0, 0, 0, 0, 0, 0, 1.3, 0,
                          8, 0, 15, 0, 0, 0, 0, 2, 0,
                          9, 40, 0, 20, 0, 0, 0, 0, 0
                          ]
        self.card_stat_count = 9
        self.card_count = 10

    def card_img_load(self):
        # card_num 별로 이미지 불러오는 부분
        cards = main_state.get_cards()
        for card in cards:
            if card.card_num == 0:
                card.image = load_image('img/Brown_Book.png')
            elif card.card_num == 1:
                card.image = load_image('img/Brown_Shield.png')
            elif card.card_num == 2:
                card.image = load_image('img/Brown_Stone.png')
            elif card.card_num == 3:
                card.image = load_image('img/Brown_Sword.png')
            elif card.card_num == 4:
                card.image = load_image('img/Blue_Knights.png')
            elif card.card_num == 5:
                card.image = load_image('img/Blue_Merlin.png')
            elif card.card_num == 6:
                card.image = load_image('img/Blue_Potion.png')
            elif card.card_num == 7:
                card.image = load_image('img/Blue_Sword.png')
            elif card.card_num == 8:
                card.image = load_image('img/Legend_Sword.png')
            elif card.card_num == 9:
                card.image = load_image('img/Legend_Treasure.png')

    def card_stat_load(self):
        # main 에서 카드 불러오기
        cards = main_state.get_cards()
        # 카드 별로 card_num, H_HP, H_ATK, H_DEF, M_HP, M_ATK, M_DEF, C_NUM 로드
        i = 0
        for card in cards:
            card.card_num = self.card_list[i * self.card_stat_count + 0]
            card.H_HP = self.card_list[i * self.card_stat_count + 1]
            card.H_ATK = self.card_list[i * self.card_stat_count + 2]
            card.H_DEF = self.card_list[i * self.card_stat_count + 3]
            card.M_HP = self.card_list[i * self.card_stat_count + 4]
            card.M_ATK = self.card_list[i * self.card_stat_count + 5]
            card.M_DEF = self.card_list[i * self.card_stat_count + 6]
            card.C_NUM = self.card_list[i * self.card_stat_count + 7]
            card.C_ACTIVATED = self.card_list[i*self.card_stat_count+8]
            i += 1
