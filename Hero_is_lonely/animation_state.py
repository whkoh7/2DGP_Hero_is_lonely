import random
import json
import os

from pico2d import *

import game_framework
import title_state
import main_state

animation = None


class Animate:
    def __init__(self):
        self.x, self.y = 0, 0
        self.image = load_image('KakaoTalk_20191008_150544563.jpg')
        self.frame = 0
        pass

    def update(self):
        if self.frame > 266:
            self.frame = 0
            game_framework.change_state(main_state)
        else:
            self.frame = self.frame + 5

    def draw(self):
        self.image.clip_draw(self.frame, 0, 800, 600, 400, 400)


name = "AnimationState"

frame = 0
cnt = 0


def enter():
    global animation
    animation = Animate()
    pass


def exit():
    global animation
    del animation


def pause():
    animation.frame = animation.frame
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def update():
    animation.update()
    pass


def draw():
    global frame
    global cnt
    clear_canvas()
    animation.draw()
    delay(0.1)
    update_canvas()