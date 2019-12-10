import random
import json
import os
import clear_state
import show_deck_state

from pico2d import *
import game_framework
import game_world

from Cards import Card
from Hero import Hero_Class
from Monster import Monster_Class
from BackGround import BackGround_Class
from BackGround import Ui_Class
from Mouse import Mouse
from Card_Deck import Deck
from Hand import Hand

Game_Size_x, Game_Size_y = 800, 800
name = "MainState"

hero = None
font = None
cards = []
monster = None
background = None
ui = None
mouse = None
deck = None
hand = None


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def enter():
    global hero
    hero = Hero_Class()
    game_world.add_object(hero, 1)

    global deck
    deck = Deck()

    global cards
    cards = [Card() for i in range(deck.card_count)]
    deck.card_stat_load()
    deck.card_img_load()
    game_world.add_objects(cards, 1)

    global monster
    monster = Monster_Class()
    game_world.add_object(monster, 1)

    global background
    background = BackGround_Class()
    game_world.add_object(background, 0)

    global ui
    ui = Ui_Class()
    game_world.add_object(ui, 0)

    global mouse
    mouse = Mouse()
    game_world.add_object(mouse, 1)
    print('change success')

    global hand
    hand = Hand()
    game_world.add_object(hand, 1)
    hand.hand_init()
    pass


def get_hero():
    return hero


def get_monster():
    return monster


def get_cards():
    return cards


def get_hand():
    return hand


def exit():
    game_world.clear()
    pass


def clear():
    game_world.clear()
    game_framework.change_state()


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
        elif event.type == SDL_MOUSEMOTION:
            mouse.x, mouse.y = event.x, Game_Size_y - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            mouse.Down = True
            mouse.Up = False
        elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            mouse.Down = False
            mouse.Up = True
        else:
            hero.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if monster.HP <= 0:
        game_framework.change_state(clear_state)

    for card in cards:
        if collide(mouse, card):
            card.click()
            if mouse.Down:
                card.del_card()
                if card.C_NUM > 0:
                    monster.hit = True
                    monster.velocity = 1
                if card.H_ATK > 0 or card.H_DEF > 0 or card.H_HP > 0:
                    hero.buf = True
                    hero.y_move = 1



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
