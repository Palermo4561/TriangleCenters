
import pygame as pg
from settings import *

def change_pause(paused:bool) -> bool:

    if paused:
        pg.mixer.music.unpause()
    else:
        pg.mixer.music.pause()

    return not paused

def setup() -> None:
    """Basic setup for the program
    
Parameters: None"""

    pg.display.set_mode((WIDTH + MENU_WIDTH, WIDTH))
    pg.display.set_caption("Triangle Centers")
    pg.display.set_icon(pg.image.load("triangle_icon.png"))

    pg.mixer.music.load("Background Music.mp3")
    pg.mixer.music.play(-1)