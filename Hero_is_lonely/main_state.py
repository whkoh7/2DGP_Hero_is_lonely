import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import animation_state
from Cards import Card
from Hero import Hero_Class
from Monster import Monster_Class
from BackGround import BackGround_Class

name = "MainState"

hero = None
font = None
card = None
monster = None
background = None


def enter():
    global hero, card, monster, background
    card = Card()
    hero = Hero_Class()
    monster = Monster_Class()
    background = BackGround_Class()
    print('change success')
    pass


def exit():
    global hero, card, monster
    del hero, card, monster
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global hero, card, monster
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
            if card.x - 100 < event.x < card.x + 100 and 800 - card.y - 100 < event.y < 800 - card.y + 100:
                print('click success')
                card.click()
        elif card.clicked is True and event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            print('button up success')
            card.Click_Up()
            monster.hp = monster.hp - hero.attack + monster.defense
            card.del_card()


def update():
    card.update()
    hero.update()
    monster.update()
    pass


def draw():
    clear_canvas()
    background.draw()
    card.draw()
    hero.draw()
    monster.draw()
    update_canvas()
