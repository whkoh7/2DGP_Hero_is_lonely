import random
import json
import os
import main_state
import title_state

from pico2d import *

import game_framework

show = None
# 배경화면 불러오는 파일, 나중에 화면 움직이는거 구현할 때 건들 예정
class Show_Class:
    def __init__(self):
        self.image = load_image('img/Card_Deck.png')
        self.bgm = load_music('img/Tribal_Affair.mp3')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(640,400)


name = "Show_Deck_State"


def enter():
    global show
    show = Show_Class()
    pass


def exit():
    global show
    del show


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(main_state)
            main_state.resume()
            print('a')

def update():
    pass


def draw():
    clear_canvas()
    show.draw()
    update_canvas()