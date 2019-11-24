from pico2d import *
from Cards import Card
import main_state

# 카드 객체를 불러와서 각각 스탯과 이미지 로드해주는 기능

class Deck:

    def __init__(self):
        # card_num, H_HP, H_ATK, H_DEF, M_HP, M_ATK, M_DEF, C_NUM 선언
        self.card_list = [0, 0, 0, 0, 0, 0, 0, 0.9,
                          1, 0, 10, 10, 0, 0, 0, 0,
                          2, 10, 0, 0, 0, 0, 0, 0,
                          3, 0, 0, 0, 0, 0, 0, 1,
                          4, 0, 15, 0, 0, 0, 0, 0,
                          ]
        pass

    def card_img_load(self):
        # card_num 별로 이미지 불러오는 부분
        cards = main_state.get_cards()
        for card in cards:
            if card.card_num == 0:
                card.image = load_image('img/Card_Sample_Small_1.png')
            elif card.card_num == 1:
                card.image = load_image('img/Card_Sample_Small_2.png')
            elif card.card_num == 2:
                card.image = load_image('img/Card.Sample_Small_3.png')
            elif card.card_num == 3:
                card.image = load_image('img/Card_Sample_Small_1.png')
            elif card.card_num == 4:
                card.image = load_image('img/Card_Sample_Small_2.png')

    def card_stat_load(self):
        # main 에서 카드 불러오기
        cards = main_state.get_cards()
        # 카드 별로 card_num, H_HP, H_ATK, H_DEF, M_HP, M_ATK, M_DEF, C_NUM 로드
        i = 0
        for card in cards:
            card.x += 240 * i
            card.card_num = self.card_list[i * 8 + 0]
            card.H_HP = self.card_list[i * 8 + 1]
            card.H_ATK = self.card_list[i * 8 + 2]
            card.H_DEF = self.card_list[i * 8 + 3]
            card.M_HP = self.card_list[i * 8 + 4]
            card.M_ATK = self.card_list[i * 8 + 5]
            card.M_DEF = self.card_list[i * 8 + 6]
            card.C_NUM = self.card_list[i * 8 + 7]
            i += 1
