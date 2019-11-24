from plistlib import Data
from pico2d import *

from Card_Deck import Deck
import main_state

class Hand:
    def __init__(self):
        self.num=5-1    #카드 총 개수 : 5개