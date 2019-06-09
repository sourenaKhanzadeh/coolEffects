import pygame
from Res.Constants import colors as CC
from Res.Constants import physics as PS
import random

# initialize PyGame.py
pygame.init()
# set the window
WIDTH = 600
HEIGHT = 600


# set the window
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
# set the title of the game
pygame.display.set_caption('Cool Effects')


def updateScreen(bg_color=CC.WHITE):
    # fill the screen
    screen.fill(bg_color)
    # update screen
    pygame.display.update()

# get PyGame pressed keys
keys = pygame.key.get_pressed()

