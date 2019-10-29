from plistlib import Data

from pico2d import *

Click_down, Click_up = range(2)

key_event_table = {
    (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): Click_down,
    (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT): Click_up,
}

next_state_table = {

}


class Hero_Class:
    image = None

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        if Hero.image is None:
            Hero.image = load_image('Penrir.png')
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state.enter(self, None)
        pass

    def add_event(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(self)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass
