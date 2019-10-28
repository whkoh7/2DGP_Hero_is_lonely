import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import animation_state

name = "MainState"

font = None
card = None


class Card:
    def __init__(self):
        self.image = load_image('Penrir.png')
        self.x, self.y = 300, 400

    def update(self):
        pass

    def click(self):
        self.image = load_image('vane.png')
        print('Click success')

    def draw(self):
        self.image.draw(self.x, self.y)


def enter():
    global card
    card = Card()
    print('change success')
    pass


def exit():
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
            card.click()


def update():
    card.update()
    pass


def draw():
    clear_canvas()
    card.draw()
    update_canvas()
