import asyncio
import pygame as pig
import js
import io
import random
import struct
import sys
import os

#Create the screen
js.document.body.style.background = 'Black'
canvas = js.window.canvas
canvas.style.outline = 'none'
canvas.width = 1920
canvas.height = 1080

#Add in Pygame/Game runner

async def main():
    window_width, window_height = 1920, 1080
    pygame.init()
    pygame.display.set_mode((window_width, window_height), flags=pygame.OPENGL | pygame.DOUBLEBUF, vsync=True)
    pygame.mixer.init()

Keys_values = {
        pygame.K_a: 'left',
        pygame.K_d: 'right',
        pygame.K_w: 'up',
        pygame.K_s: 'down',
        pygame.K_LEFT: 'left',
        pygame.K_RIGHT: 'right',
        pygame.K_UP: 'up',
        pygame.K_DOWN: 'down',
        pygame.K_q: 'turn_left',
        pygame.K_e: 'turn_right',
        pygame.K_SPACE: 'space',
        pygame.K_ESCAPE: 'escape',
        pygame.K_BACKSPACE: 'escape',
        pygame.K_LCTRL: 'catch',
        1: 'define',
        }
  


