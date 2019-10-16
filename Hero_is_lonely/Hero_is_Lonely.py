from pico2d import *
import random

# Game object class here
#Cards
class Card:
    def __init__(self):
        self.x,self.y=300,300
    def draw(self):
        pass
    pass

#Hero
class Hero:
    def __init__(self):
        self.x, self.y = 600.300
        self.frame = random.randint(0,7)
        #self.image = load_image('')

    def update(self):
        #self.frame = (self.frame + 1) % 8
        pass
    def draw(self):

        #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        pass

class Boss:
    def __init__(self):
        self.x, self.y = 600.300
        self.frame = random.randint(0,7)
        #self.image = load_image('')

    def update(self):
        #self.frame = (self.frame + 1) % 8
        pass
    def draw(self):

        #self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        pass

def handle_events():
    global game
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game = False


# initialization code
open_canvas()
game = True

# game main loop code
while game:
    handle_events()
    clear_canvas()
    update_canvas()

    delay(0.05)
# finalization code
close_canvas()