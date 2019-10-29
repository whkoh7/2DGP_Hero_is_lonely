import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import animation_state
from Hero import Hero_Class

name = "MainState"

hero = None
font = None





def enter():
    global card
    card = Card()
    hero = Hero_Class()
    print('change success')
    pass


def exit():
    global hero
    del hero
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global card
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            pause()
            game_framework.push_state(pause_state)
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if -250 < event.x < 350 and 350 < event.y < 450:
                print('click success')
                card.click()
        elif 250 < event.x < 350 and 150 < event.y < 250:
            card.OntheMouse()
        elif (event.x <= 250 or event.x >= 350) and (event.y <= 150 or event.y >= 250):
            card.Mouse_is_Out()


def update():
    card.update()
    pass


def draw():
    clear_canvas()
    card.draw()
    update_canvas()
