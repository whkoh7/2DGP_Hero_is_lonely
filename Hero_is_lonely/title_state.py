import game_framework
from pico2d import *

import main_state
import animation_state
name = "TitleState"
image = None


def enter():
    global image
    image = load_image('sm_5aba147bcacf2.png')
    pass


def exit():
    global image
    del (image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(animation_state)
    pass


def draw():
    clear_canvas()
    image.draw(400, 400)
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass
