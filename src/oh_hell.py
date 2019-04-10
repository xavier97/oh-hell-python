# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame, sys, os
from pygame.locals import *


# ------------------- ASSETS -------------------
# Images
DEFAULT_ICON = os.path.join('../assets/images/', 'icon-fire.png')

# FONTS
DEFAULT_FONT = os.path.join('../assets/fonts/', 'freesansbold.tff')

# Colors
BLACK   = (0, 0, 0, 0)
WHITE   = (255, 255, 255, 255)
BEIGE   = (245, 245, 220)
RED     = (255, 0, 0)
GREEN   = pygame.Color(0, 255, 0)
BLUE    = pygame.Color(0, 0, 255)


# ----------------------------------------------

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

# Window set-up
screen_width  =   0
screen_height = 700

pygame.init()
icon_surf = pygame.image.load(DEFAULT_ICON)
pygame.display.set_icon(icon_surf)
DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Oh Hell!')


# Draw a button
text = pygame.font.SysFont(DEFAULT_FONT, 32)
TextSurf, TextRect = text_objects("A bit Racey", text)
TextRect.center = (200, 150)

# draw on the surface oject
DISPLAYSURF.fill(BEIGE)


while True: # main game loop
    DISPLAYSURF.blit(TextSurf, TextRect)
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            #sys.exit()
            exit()
    pygame.display.update()