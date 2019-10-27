import random
import json
import os

from pico2d import *

import game_framework
import main_state

pauseImg = None

frame = 0
cnt = 0


def enter():
    pass


def exit():
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()
            main_state.resume()


def update(): pass


def draw():
    global frame
    global cnt
    clear_canvas()

    update_canvas()