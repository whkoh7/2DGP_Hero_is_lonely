from plistlib import Data
from pico2d import *

from Card_Deck import Deck
from Cards import Card
import main_state
from random import *

deck = None
deck = Deck()


class Hand:
    global deck

    def __init__(self):
        self.num = 5  # 카드 총 개수 : 5개
        self.location_x = [150, 390, 630, 870, 1110]
        self.location_y = 200
        self.hand = [100, 100, 100, 100, 100]
        pass

    def hand_init(self):
        cards = main_state.get_cards()
        for i in range(5):
            if self.hand[i] is 100:
                num = randint(0, deck.card_count - 1)
                while num in self.hand:
                    num = randint(0, deck.card_count - 1)
                if num not in self.hand:
                    self.hand[i] = num


            print(i, self.hand[i])

        for card in cards:
            for i in range(5):
                if self.hand[i] is card.card_num:
                    card.C_ACTIVATED = 1
                    card.x = self.location_x[i]
                    print(i, card.x)

    def update(self):
        pass

    def draw(self):
        pass
