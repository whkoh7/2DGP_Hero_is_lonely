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
        if Hero_Class.image is None:
            Hero_Class.image = load_image('pumpkin_dude.png')
        self.frame = 0
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        pass

    def add_event(self, event):
        pass

    def update(self):
        self.frame = (self.frame +1)% 8
        self.x += 2
        pass

    def draw(self):
        self.image.clip_draw(self.frame*16,0,16,32,self.x,self.y)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass
