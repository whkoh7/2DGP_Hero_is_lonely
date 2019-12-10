import game_framework
import pico2d
# fill here
import main_state
import start_state
import animation_state
import title_state

pico2d.open_canvas(1280,800)
game_framework.run(title_state)
pico2d.close_canvas()