# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""    
import pygame, sys, os, math, random
from pygame.locals import *
from gameLib import cardGame

class Card:
    card_name = ""
    posx = 0
    posy = 0
    
    def __init__(self, posx, posy, card_name):
        self.posx = posx
        self.posy = posy
        self.card_name = card_name
    
    def display_card(self):
        path = os.path.join('../assets/images/cards', self.card_name + '.gif')
        card_image = pygame.image.load(path)
        return card_image
    
#GAMEPLAY LOGIC FUNCTIONS
#-----------------------------------------------------------------------------
def viewField():
    print("\nFIELD: \n---------------------------------")
    fieldObj.toStringDeck()
    print("Suit asked: " + suitAsked.upper())
    print("Trump: " + trump.upper())
    print("---------------------------------")

def showHand():
    print("\n YOUR HAND:")
    player1.viewHand()

def computerTurn(comp):
    global fieldObj
    global suitAsked
    #If first card played then pick random card from hand to play
    if(suitAsked == None):
        cardPlayed = comp.discard(random.choice(range(len(comp.hand))))
        fieldObj.addCard(cardPlayed)
        suitAsked = cardPlayed.getSuit()
    #Else discard by suit asked
    else:
        cardPlayed = comp.discardBySuit(suitAsked)
        fieldObj.addCard(cardPlayed)
        
def playerTurn(player):
    global suitAsked
    validPlay = False
    #Check if play is valid
    while(not validPlay):
        validCard = False
        #Check if card choice is valid
        while(not validCard):
            cardChoice = int(input("Enter card to play: "))
            if((cardChoice < 0) or (cardChoice > len(player.hand)-1)):
                print("Error: Input not in range of hand")
            else:
                validCard = True
        
        #If first card played then card choice is automatically valid
        if(suitAsked == None):
            suitAsked = player.hand[cardChoice].getSuit()
            break
            
        validPlay = player.checkPlay(cardChoice, suitAsked)
        if(not validPlay):
            print("Play is not valid. Must play suit asked!")
     
    
    #Discard from hand and add card to field
    fieldObj.addCard(player.discard(cardChoice))

#BIDDING
#*****************************************************************************
#*****************************************************************************    
def playerBid(player):
    while(True):
        bid = int(input("\nEnter your bid for this round: "))
        if((bid >= 0) and (bid <= cardsNum)):
            break
        else:
            print("Error: Please enter bid between 0 and " + str(cardsNum))
    player1.setBid(bid)

def p1StartBid():
    playerBid(player1)
    #Computer bids
    try:
        comPlayer2.setBid(random.choice(range(5)))
        comPlayer3.setBid(random.choice(range(5)))
        comPlayer4.setBid(random.choice(range(5)))
    except IndexError:
        comPlayer2.setBid(random.choice(range(cardsNum)))
        comPlayer3.setBid(random.choice(range(cardsNum)))
        comPlayer4.setBid(random.choice(range(cardsNum)))
    #Last Bid Check
    while(True):
        bidSum = player1.getBid() + comPlayer2.getBid() + comPlayer3.getBid() + comPlayer4.getBid()
        if(bidSum == cardsNum):
            comPlayer4.setBid(random.choice(range(cardsNum)))
        else:
            break
        
def p2StartBid():
    #Computer bids
    try:
        comPlayer2.setBid(random.choice(range(5)))
        comPlayer3.setBid(random.choice(range(5)))
        comPlayer4.setBid(random.choice(range(5)))
    except IndexError:
        comPlayer2.setBid(random.choice(range(cardsNum)))
        comPlayer3.setBid(random.choice(range(cardsNum)))
        comPlayer4.setBid(random.choice(range(cardsNum)))
    playerBid(player1)
    #Last Bid Check
    while(True):
        bidSum = player1.getBid() + comPlayer2.getBid() + comPlayer3.getBid() + comPlayer4.getBid()
        if(bidSum == cardsNum):
            print("Sum of all bids cannot equal number of cards in hand!")
            playerBid(player1)
        else:
            break
    
def p3StartBid():
    #Bids
    try:
        comPlayer3.setBid(random.choice(range(5)))
        comPlayer4.setBid(random.choice(range(5)))
        playerBid(player1)
        comPlayer2.setBid(random.choice(range(5)))
    except IndexError:
        comPlayer3.setBid(random.choice(range(cardsNum)))
        comPlayer4.setBid(random.choice(range(cardsNum)))
        playerBid(player1)
        comPlayer2.setBid(random.choice(range(5)))
    #Last Bid Check
    while(True):
        bidSum = player1.getBid() + comPlayer2.getBid() + comPlayer3.getBid() + comPlayer4.getBid()
        if(bidSum == cardsNum):
            comPlayer2.setBid(random.choice(range(cardsNum)))
        else:
            break
    
def p4StartBid():
    #Bids
    try:
        comPlayer4.setBid(random.choice(range(5)))
        playerBid(player1)
        comPlayer2.setBid(random.choice(range(5)))
        comPlayer3.setBid(random.choice(range(5)))
    except IndexError:
        comPlayer4.setBid(random.choice(range(cardsNum)))
        playerBid(player1)
        comPlayer2.setBid(random.choice(range(5)))
        comPlayer3.setBid(random.choice(range(5)))
    #Last Bid Check
    while(True):
        bidSum = player1.getBid() + comPlayer2.getBid() + comPlayer3.getBid() + comPlayer4.getBid()
        if(bidSum == cardsNum):
            comPlayer3.setBid(random.choice(range(cardsNum)))
        else:
            break
#*****************************************************************************
#*****************************************************************************
    
def playTrick():
    if(trickStarter == "p1"):
        print("You play first! Pick any card to start the trick")
        showHand()
        playerTurn(player1)
        computerTurn(comPlayer2)
        computerTurn(comPlayer3)
        computerTurn(comPlayer4)
    elif(trickStarter == "p2"):
        print("Player 2 starts the trick")
        computerTurn(comPlayer2)
        computerTurn(comPlayer3)
        computerTurn(comPlayer4)
        viewField()
        showHand()
        playerTurn(player1)
    elif(trickStarter == "p3"):
        print("Player 3 starts the trick")
        computerTurn(comPlayer3)
        computerTurn(comPlayer4)
        viewField()
        showHand()
        playerTurn(player1)
        computerTurn(comPlayer2)
    elif(trickStarter == "p4"):
        print("Player 4 starts the trick")
        computerTurn(comPlayer4)
        viewField()
        showHand()
        playerTurn(player1)
        computerTurn(comPlayer2)
        computerTurn(comPlayer3)
        
def resolveTrick():
    global suitAsked
    winningSuit = suitAsked
    winningVal = 0
    winningCard = None
    for card in fieldObj.mydeck:
        #If card is trump
        if(card.getSuit() == trump):
            #If current winning card isn't trump automatic win
            if(winningSuit != trump):
                winningCard = card
                winningSuit = trump
                winningVal = card.getVal()
            #If current winning card is also trump check values 
            elif(card.getVal() > winningVal):
                winningCard = card
                winningVal = card.getVal()
        #If card is suit asked
        elif(card.getSuit() == suitAsked):
            if((winningSuit != trump) and (card.getVal() > winningVal)):
                winningCard = card
                winningVal = card.getVal()
   
    #Check which player played the winning card and give them the trick             
    if(player1.getPlayerID() == winningCard.getTagID()):
        player1.addTrick()
    elif(comPlayer2.getPlayerID() == winningCard.getTagID()):
        comPlayer2.addTrick()
    elif(comPlayer3.getPlayerID() == winningCard.getTagID()):
        comPlayer3.addTrick()
    elif(comPlayer4.getPlayerID() == winningCard.getTagID()):
        comPlayer4.addTrick()
    
    #Send cards in field back to deck
    for i in range(4):
        deckObj.addCard(fieldObj.drawCard())
    
    #Player who won trick starts next round
    global trickStarter
    trickStarter = winningCard.getTagID()
    print("*** " + trickStarter + " won the trick! ***")
    print("END OF TRICK")
    print("************************************")
    #Reset suitAsked
    suitAsked = None
     
def resolveRound():
    #Check if bids match number of tricks won. If they do give that player points
    if(player1.getTricks() == player1.getBid()):
        player1.addPoints(player1.getBid() + 10)
    if(comPlayer2.getTricks() == comPlayer2.getBid()):
        comPlayer2.addPoints(comPlayer2.getBid() + 10)
    if(comPlayer3.getTricks() == comPlayer3.getBid()):
        comPlayer3.addPoints(comPlayer3.getBid() + 10)
    if(comPlayer4.getTricks() == comPlayer4.getBid()):
        comPlayer4.addPoints(comPlayer4.getBid() + 10)
        
    player1.clearTricks()
    comPlayer2.clearTricks()
    comPlayer3.clearTricks()
    comPlayer4.clearTricks()
    
    #Move starting player to the left for next round
    global roundStarter
    global trickStarter
    if(roundStarter == "p1"):
        roundStarter = "p2"
        trickStarter = "p2"
    elif(roundStarter == "p2"):
        roundStarter = "p3"
        trickStarter = "p3"
    elif(roundStarter == "p3"):
        roundStarter = "p4"
        trickStarter = "p4"
    elif(roundStarter == "p4"):
        roundStarter = "p1"
        trickStarter = "p1"
        
    
    print("LEADERBOARD:")
    print("Player1: " + str(player1.getPoints()))
    print("Player2: " + str(comPlayer2.getPoints()))
    print("Player3: " + str(comPlayer3.getPoints()))
    print("Player4: " + str(comPlayer4.getPoints()))
    print("************************************")
#-----------------------------------------------------------------------------       
        
#GLOBALS
#-----------------------------------------------------------------------------
deckObj = cardGame.deck()
fieldObj = cardGame.deck()
player1 = cardGame.player("p1")
comPlayer2 = cardGame.player("p2")
comPlayer3 = cardGame.player("p3")
comPlayer4 = cardGame.player("p4")
trickStarter = "p2" #keeps track of who starts the next trick
roundStarter = "p2" #Player2 starts round 1
suitAsked = None
roundNum = 1
cardsNum = 13
trump = None
done = False
#-----------------------------------------------------------------------------

# ------------------- ASSETS -------------------
# Window set-up
screen_width  = 1280
screen_height = 700

# Image Locations
DEFAULT_ICON = os.path.join('../assets/images/', 'icon-fire.png')
C2_PATH = os.path.join('../assets/images/cards', 'C2.gif')
C3_PATH = os.path.join('../assets/images/cards', 'C3.gif')
BACK_PATH = os.path.join('../assets/images/cards', 'back.gif')

# Load Images
icon_surf = pygame.image.load(DEFAULT_ICON)
C2 = pygame.image.load(C2_PATH)
C3 = pygame.image.load(C3_PATH)
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
GRAY = (128, 128, 128)

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
    click = pygame.mouse.get_pressed() # Get mouse click
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            action() 
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
    
def opponent_play():
    opponent_card_list = ["DA", "H2", "SK"] # cards each opponent chose to play
    
    # Opponent 1
    angle = 90
    card = Card(439, 275, opponent_card_list[0])
    new_card = pygame.transform.rotate(card.display_card(), angle)
    DISPLAYSURF.blit(new_card, (card.posx, card.posy))
    
    # Opponent 2
    angle = 180
    card = Card(560, 202, opponent_card_list[1])
    new_card = pygame.transform.rotate(card.display_card(), angle)
    DISPLAYSURF.blit(new_card, (card.posx, card.posy))
    
    # Opponent 3
    angle = 90
    card = Card(657, 275, opponent_card_list[2])
    new_card = pygame.transform.rotate(card.display_card(), angle)
    DISPLAYSURF.blit(new_card, (card.posx, card.posy))
    
    
def trump_card(card_image):
    newLabel("", 845, 40, 83, 107, RED)
    newLabel("Trump Card", 820, 152, 140, 30, RED)
    DISPLAYSURF.blit(card_image, (850, 45))
    
def card_button(card, action=None):
    w =  77
    h = 101
    x = card.posx
    y = card.posy
    pygame.draw.rect(DISPLAYSURF, BEIGE, (x , y , w , h)) # display button frame

    mouse = pygame.mouse.get_pos() # Get mouse's location
    click = pygame.mouse.get_pressed() # Get mouse click
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF, BRIGHT_RED, (x, y, w, h))
        if click[0] == 1 and action != None:
            send_card_action(card)
    else:
        pygame.draw.rect(DISPLAYSURF, BEIGE, (x, y, w, h))

def newLabel(msg, x, y, w, h, background_color, text_color=BLACK):
    pygame.draw.rect(DISPLAYSURF, background_color, (x , y , w , h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText, text_color)
    textRect.center = ( (x + (w / 2)), ( y + (h / 2)) )
    DISPLAYSURF.blit(textSurf, textRect)
    
# ------------------- ACTION EVENTS -------------------
def send_card_action(card):
    DISPLAYSURF.blit(card.display_card(), (560, 323))
        
def quit_action():
    pygame.draw.rect(DISPLAYSURF, GRAY, (439 , 202, 315, 218))
# -----------------------------------------------------

while True: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            exit()

    card1 = Card(198, 461, "CA")

    # Player's card spots
    card_button(card1, send_card_action)
    #card_button(278, 461, send_card_action)
    #card_button(358, 461, send_card_action)
    #card_button(438, 461, send_card_action)
    #card_button(518, 461, send_card_action)
    #card_button(598, 461, send_card_action)
    #card_button(678, 461, send_card_action)
    #card_button(758, 461, send_card_action)
    #card_button(838, 461, send_card_action)
    #card_button(918, 461, send_card_action)
    
    # Displaying cards in hand
    cardx1 = 200
    cardy1 = 463
    DISPLAYSURF.blit(C2, (cardx1, cardy1))
    
    # Opponent's hands
    opponent_cards(1, 10)
    opponent_cards(2, 10)
    opponent_cards(3, 10)
    
    # Opponent take their turn
    opponent_play()
    
    # Trump Card
    trump_card(C3)
    
    # Bottom toolbar
    toolbarSurf = pygame.draw.rect(DISPLAYSURF, BLACK, (0, 630, 1280, 70))
    newLabel("Round:", 40, 640, 160, 50, BLACK, RED)
    round = 10 # TEST
    newLabel(str(round), 160, 640, 40, 50, BLACK, RED)
    newLabel("Points:", 280, 640, 160, 50, BLACK, RED)
    points = 100 # TEST
    newLabel(str(points), 400, 640, 40, 50, BLACK, RED)
    newButton("Instructons", 920, 640, 240, 50, BLUE, RED, action=None)
    newButton("Quit", 1200, 640, 60, 50, BLUE, RED, action=quit_action)
    
    fpsClock.tick(60)
    pygame.display.update()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    