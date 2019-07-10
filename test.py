"""Experimenting with pyglet and procedural generation."""
import math

import numpy as np
import pyglet
from pyglet.window import key, mouse

from pyglet.gl import *

FPS = 60.0
BLOCK_SIZE = 16
world: dict = {}  # (x,y), texture


def generate_world(max_hight, max_width: int):
    """Fill world dict."""
    for x in range(0, max_width, BLOCK_SIZE):
        for y in range(0, max_hight, BLOCK_SIZE):
            world[(x, y)] = "DIRT"
    # print(world)


win = pyglet.window.Window(width=800, height=600, fullscreen=False)
dirt = pyglet.resource.image("assets/dirt.png")
player_img = pyglet.resource.image("assets/player_blip.png")
player = {"x": win.width // 2, "y": win.height // 2}


def update(dt):
    print(dt)  # time elapsed since last time we were called
    label.x = position["x"]
    label.y = position["y"]


position = dict(x=0, y=0)


@win.event
def on_key_press(symbol, modifiers):
    if symbol == key.RIGHT:
        player["x"] += BLOCK_SIZE
    elif symbol == key.LEFT:
        player["x"] -= BLOCK_SIZE


@win.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        label.x = x
        label.y = y


@win.event
def on_draw():
    win.clear()
    for pnt in world:
        dirt.blit(pnt[0], pnt[1])
    player_img.blit(player["x"], player["y"])


generate_world(win.height // 2, win.width)
# pyglet.clock.schedule_interval(update, 1 / FPS)
pyglet.app.run()
