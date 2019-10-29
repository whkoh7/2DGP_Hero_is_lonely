import game_framework
import pico2d
# fill here
import main_state
import start_state

pico2d.open_canvas(800,800)
game_framework.run(start_state)
pico2d.close_canvas()