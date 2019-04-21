# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame, sys, os, math
from pygame.locals import *

# ------------------- ASSETS -------------------
# Window set-up
screen_width  = 1280
screen_height = 700

# Image Locations
DEFAULT_ICON = os.path.join('../assets/images/', 'icon-fire.png')
C2_PATH = os.path.join('../assets/images/cards', 'C2.gif')
BACK_PATH = os.path.join('../assets/images/cards', 'back.gif')

# Load Images
icon_surf = pygame.image.load(DEFAULT_ICON)
C2 = pygame.image.load(C2_PATH)
back = pygame.image.load(BACK_PATH)

# FONTS
DEFAULT_FONT = os.path.join('../assets/fonts/', 'AndaleMono.tff')

# Colors
BLACK   = (0, 0, 0, 0)
WHITE   = (255, 255, 255, 255)
BEIGE   = (245, 245, 220)
RED     = (200, 0, 0)
GREEN   = pygame.Color(0, 200, 0)
BLUE    = pygame.Color(0, 0, 200)
YELLOW  = pygame.Color(255, 255, 0)
BRIGHT_RED   = (255,0,0)
BRIGHT_GREEN = (0,255,0)

fps = 60
fpsClock = pygame.time.Clock()

# ----------------------------------------------

# Initialization
pygame.init()
pygame.display.set_icon(icon_surf)
DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height))
DISPLAYSURF.fill(BEIGE) # Background Color
pygame.display.set_caption('Oh Hell!')

def text_objects(text, font, text_color=BLACK):
    textSurface = font.render(text, True, text_color)
    return textSurface, textSurface.get_rect()

def newButton(msg, x, y, w, h, inactive_color, active_color, action=None):
    pygame.draw.rect(DISPLAYSURF, inactive_color, (x , y , w , h)) # display button frame
    
    mouse = pygame.mouse.get_pos() # Get mouse's location
    #click = pygame.mouse.get_pressed() # Get mouse click
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF, active_color, (x, y, w, h))
        #if click[0] == 1 and action != None:
        #    action() 
    else:
        pygame.draw.rect(DISPLAYSURF, inactive_color, (x, y, w, h))
        
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x + (w / 2)), ( y + (h / 2)) )
    DISPLAYSURF.blit(textSurf, textRect)
    
def opponent_cards(opponent_id, opponent_num_cards):
    
    if (opponent_id == 1):
        angle = 90
        newBack = pygame.transform.rotate(back, angle)
        DISPLAYSURF.blit(newBack, (80, 382))
        DISPLAYSURF.blit(newBack, (80, 350))
        DISPLAYSURF.blit(newBack, (80, 318))
        DISPLAYSURF.blit(newBack, (80, 286))
        DISPLAYSURF.blit(newBack, (80, 254))
        DISPLAYSURF.blit(newBack, (80, 222))
        DISPLAYSURF.blit(newBack, (80, 190))
        DISPLAYSURF.blit(newBack, (80, 158))
        DISPLAYSURF.blit(newBack, (80, 126))
        DISPLAYSURF.blit(newBack, (80,  94))
    elif (opponent_id == 2):
        angle = 270
        newBack = pygame.transform.rotate(back, angle)
        DISPLAYSURF.blit(newBack, (1020, 382))
        DISPLAYSURF.blit(newBack, (1020, 350))
        DISPLAYSURF.blit(newBack, (1020, 318))
        DISPLAYSURF.blit(newBack, (1020, 286))
        DISPLAYSURF.blit(newBack, (1020, 254))
        DISPLAYSURF.blit(newBack, (1020, 222))
        DISPLAYSURF.blit(newBack, (1020, 190))
        DISPLAYSURF.blit(newBack, (1020, 158))
        DISPLAYSURF.blit(newBack, (1020, 126))
        DISPLAYSURF.blit(newBack, (1020,  94))
    elif (opponent_id == 3):
        angle = 180
        newBack = pygame.transform.rotate(back, angle)
        DISPLAYSURF.blit(newBack, (320, 45))
        DISPLAYSURF.blit(newBack, (360, 45))
        DISPLAYSURF.blit(newBack, (400, 45))
        DISPLAYSURF.blit(newBack, (440, 45))
        DISPLAYSURF.blit(newBack, (480, 45))
        DISPLAYSURF.blit(newBack, (520, 45))
        DISPLAYSURF.blit(newBack, (560, 45))
        DISPLAYSURF.blit(newBack, (600, 45))
        DISPLAYSURF.blit(newBack, (640, 45))
        DISPLAYSURF.blit(newBack, (680, 45))
    
def trump_card():
    newLabel("", 845, 40, 83, 107, RED)
    newLabel("Trump Card", 820, 152, 140, 30, RED)
    DISPLAYSURF.blit(C2, (850, 45))
    
def send_card_action():
    print("Hello")
    pass
        
    
def card_button(buttonx, buttony, action=None):
    w =  77
    h = 101
    pygame.draw.rect(DISPLAYSURF, BEIGE, (buttonx , buttony , w , h)) # display button frame

    mouse = pygame.mouse.get_pos() # Get mouse's location
    click = pygame.mouse.get_pressed() # Get mouse click
    
    if buttonx + w > mouse[0] > buttonx and buttony + h > mouse[1] > buttony:
        pygame.draw.rect(DISPLAYSURF, BRIGHT_RED, (buttonx, buttony, w, h))
        if click[0] == 1 and action != None:
            send_card_action()
    else:
        pygame.draw.rect(DISPLAYSURF, BEIGE, (buttonx, buttony, w, h))

def newLabel(msg, x, y, w, h, background_color, text_color=BLACK):
    pygame.draw.rect(DISPLAYSURF, background_color, (x , y , w , h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText, text_color)
    textRect.center = ( (x + (w / 2)), ( y + (h / 2)) )
    DISPLAYSURF.blit(textSurf, textRect)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            exit()
    
    # Bottom toolbar
    toolbarSurf = pygame.draw.rect(DISPLAYSURF, BLACK, (0, 630, 1280, 70))
    newLabel("Round:", 40, 640, 160, 50, BLACK, RED)
    round = 10 # TEST
    newLabel(str(round), 160, 640, 40, 50, BLACK, RED)
    newLabel("Points:", 280, 640, 160, 50, BLACK, RED)
    points = 100 # TEST
    newLabel(str(points), 400, 640, 40, 50, BLACK, RED)

    # Player's card spots
    card_button(198, 461, send_card_action)
    #card_button(278, 461, cardx1, cardy1)
    #card_button(358, 461, cardx1, cardy1)
    #card_button(438, 461, cardx1, cardy1)
    #card_button(518, 461, cardx1, cardy1)
    #card_button(598, 461, cardx1, cardy1)
    #card_button(678, 461, cardx1, cardy1)
    #card_button(758, 461, cardx1, cardy1)
    #card_button(838, 461, cardx1, cardy1)
    #card_button(918, 461, cardx1, cardy1)
    
    # Displaying cards in hand
    cardx1 = 200
    cardy1 = 463
    DISPLAYSURF.blit(C2, (cardx1, cardy1))
    
    # Opponent's hands
    opponent_cards(1, 10)
    opponent_cards(2, 10)
    opponent_cards(3, 10)
    
    # Trump Card
    trump_card()
    
    fpsClock.tick(60)
    pygame.display.update()
    
    
class card:
    posx = 0
    posy = 0
    
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
    
    def display_card(self, card_name):
        path = os.path.join('../assets/images/cards', card_name + '.gif')
        card_image = pygame.image.load(path)
        DISPLAYSURF.blit(card_image, (self.posx, self.posy))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    