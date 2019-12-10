import random
import json
import os
import main_state

from pico2d import *

import game_framework

clear = None
# 배경화면 불러오는 파일, 나중에 화면 움직이는거 구현할 때 건들 예정
class Clear_Class:
    def __init__(self):
        self.image = load_image('img/Stage_Clear.png')
        self.bgm = load_music('img/Tribal_Affair.mp3')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(640,400)


name = "ClearState"


def enter():
    global clear
    clear = Clear_Class()
    pass


def exit():
    global clear
    del clear


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def update():
    pass


def draw():
    clear_canvas()
    clear.draw()
    update_canvas()