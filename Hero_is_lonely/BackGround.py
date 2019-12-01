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


ui_names = ['Box', 'Exit', 'Pause']
ui_pos = [215, 470, 1100, 750, 1000, 750]


class Ui_Class:
    images = None

    def load_image(self):
        if Ui_Class.images is None:
            Ui_Class.images = {}
            for name in ui_names:
                Ui_Class.images[name] = [load_image("img/" + name + "_UI_img.png")]

    def __init__(self):
        self.box_x_size = 150
        self.box_y_size = 200
        self.ui_x_size =69
        self.ui_y_size =67
        self.load_image()

    def update(self):
        pass

    def draw(self):
        Ui_Class.images['Box'][0].draw(ui_pos[0], ui_pos[1], self.box_x_size, self.box_y_size)
        Ui_Class.images['Box'][0].draw(ui_pos[0]+875, ui_pos[1], self.box_x_size, self.box_y_size)
        Ui_Class.images['Exit'][0].draw(ui_pos[2],ui_pos[3],self.ui_x_size,self.ui_y_size)
        Ui_Class.images['Pause'][0].draw(ui_pos[4],ui_pos[5],self.ui_x_size,self.ui_y_size)

