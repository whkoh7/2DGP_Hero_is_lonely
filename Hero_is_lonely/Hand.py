from plistlib import Data
from pico2d import *

from Card_Deck import Deck
from Cards import Card
import main_state


class Hand:
    def __init__(self):
        self.num = 5  # 카드 총 개수 : 5개
        self.location_x = [150, 390, 630, 870, 1110]
        self.location_y = 200

        pass
