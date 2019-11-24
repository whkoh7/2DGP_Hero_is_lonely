from plistlib import Data
from pico2d import *

# 배경화면 불러오는 파일, 나중에 화면 움직이는거 구현할 때 건들 예정
class BackGround_Class:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('img/Background_Sample.jpg')
        self.frame = 0
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(100, 0, 1280, 800, 640, 400)