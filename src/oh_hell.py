# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""    
import pygame, sys, os, math, random, time
import threading
from pygame.locals import *
from gamelib import cardGame

'''
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
'''
    
#GAMEPLAY LOGIC FUNCTIONS
#-----------------------------------------------------------------------------
def viewField():
    print("\nFIELD: \n---------------------------------")
    fieldObj.toStringDeck()
    print("Suit asked: " + suitAsked.upper())
    print("Trump: " + trump.upper())
    print("---------------------------------")

def showHand():
    count = 1
    for card in player1.hand:
        try:
            DISPLAYSURF.blit(card.displayCard(), playerPositionDict.get('pos' + str(count)))
            count += 1
        except TypeError:
            pass
    #Delete after image of cards no longer in hand
    while(count <= 10):
        posx = playerPositionDict.get('pos' + str(count))[0]
        posy = playerPositionDict.get('pos' + str(count))[1]
        pygame.draw.rect(DISPLAYSURF, FELT_GREEN, (posx-2, posy-2, 77, 101))
        count += 1

def computerTurn(comp):
    global fieldObj
    global suitAsked
    #If first card played then pick random card from hand to play
    if(suitAsked == None):
        randIndex = random.choice(range(len(comp.hand)))
        #print("random index: " + str(randIndex))
        cardPlayed = comp.discard(comp.hand[randIndex].getCard())
        fieldObj.addCard(cardPlayed)
        suitAsked = cardPlayed.getSuit()
    #Else discard by suit asked
    else:
        cardPlayed = comp.discardBySuit(suitAsked)
        fieldObj.addCard(cardPlayed)
        
    print(comp.getPlayerID() + " played the  " + cardPlayed.getCard())
    
    if(comp.playerID == 'p2'):
        #Computer 2
        angle = 90
        #card = cardGame.card("diamonds", 14)
        cardPlayed.updateCardPosition((439, 275))
        rotated_card = pygame.transform.rotate(cardPlayed.displayCard(), angle)
        DISPLAYSURF.blit(rotated_card, (cardPlayed.posx, cardPlayed.posy))
    elif(comp.playerID == 'p3'):
        #Computer 3
        angle = 180
        #card = cardGame.card("hearts", 2)
        cardPlayed.updateCardPosition((560, 202))
        rotated_card = pygame.transform.rotate(cardPlayed.displayCard(), angle)
        DISPLAYSURF.blit(rotated_card, (cardPlayed.posx, cardPlayed.posy))
    elif(comp.playerID == 'p4'):
        #Computer 4
        angle = 90
        #card = cardGame.card("spades", 13)
        cardPlayed.updateCardPosition((657, 275))
        rotated_card = pygame.transform.rotate(cardPlayed.displayCard(), angle)
        DISPLAYSURF.blit(rotated_card, (cardPlayed.posx, cardPlayed.posy))   

'''        
def playerTurn(player):
    global suitAsked
    validPlay = False
    #Check if play is valid
    while(not validPlay):
        #Check if card choice is valid
        while(True):
            card_button(player1.hand[0], 'pos1', send_card_action)
            card_button(player1.hand[1], 'pos2', send_card_action)
            card_button(player1.hand[2], 'pos3', send_card_action)
            card_button(player1.hand[3], 'pos4', send_card_action)
            card_button(player1.hand[4], 'pos5', send_card_action)
            card_button(player1.hand[5], 'pos6', send_card_action)
            card_button(player1.hand[6], 'pos7', send_card_action)
            card_button(player1.hand[7], 'pos8', send_card_action)
            card_button(player1.hand[8], 'pos9', send_card_action)
            card_button(player1.hand[9], 'pos10', send_card_action)
            showHand()
            fpsClock.tick(60)
            pygame.display.update()
        
        #If first card played then card choice is automatically valid
        if(suitAsked == None):
            suitAsked = player.hand[cardChoice].getSuit()
            break
            
        validPlay = player.checkPlay(cardChoice, suitAsked)
        if(not validPlay):
            print("Play is not valid. Must play suit asked!")
     
    
    #Discard from hand and add card to field
    fieldObj.addCard(player.discard(cardChoice))
'''    
def checkValidity(card, index):
    global suitAsked
    #If first card played then card choice is automatically valid
    if(suitAsked == None):
        suitAsked = card.getSuit()
        return True
            
    return player1.checkPlay(index, suitAsked)

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
    
def playTrick(starter):
    global playerTurn
    global doneWithTurn
    global waiting
    if(playerTurn == 'p1'):
        try:
            #Generate card buttons
            for i in range(len(player1.hand)):
                card_button(player1.hand[i], 'pos'+str(i+1), i, send_card_action)
        except IndexError: pass
    elif(playerTurn == 'p2' and not waiting):
        computerTurn(comPlayer2)
        #playerTurn = 'p3'
        waiting = True
    elif(playerTurn == 'p3' and not waiting):
        computerTurn(comPlayer3)
        #playerTurn = 'p4'
        waiting = True
    elif(playerTurn == 'p4' and not waiting):
        computerTurn(comPlayer4)
        #playerTurn = 'p1'
        waiting = True
        
    if(starter == 'p1' and playerTurn == 'p4'):
        resolveTrick()
    elif(starter == 'p2' and playerTurn == 'p1' and doneWithTurn == True):
        resolveTrick()
        doneWithTurn = False
    elif(starter == 'p3' and playerTurn == 'p2'):
        resolveTrick()
    elif(starter == 'p4' and playerTurn == 'p3'):
        resolveTrick()

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
        
    #Clear the visible field
    pygame.draw.rect(DISPLAYSURF, FELT_GREEN, (439 , 202, 315, 218))
    
    #Player who won trick starts next round
    global trickStarter
    global playerTurn
    global firstTrickOfRound
    if(firstTrickOfRound):
        firstTrickOfRound = False
    trickStarter = winningCard.getTagID()
    playerTurn = trickStarter
    print("*** " + trickStarter + " won the trick! ***")
    print("Computer hand: " + str(len(comPlayer2.hand)))
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

# ------------------- ASSETS -------------------
# Window set-up
screen_width  = 1280
screen_height = 700

# Image Locations
DEFAULT_ICON = os.path.join('../assets/images/', 'icon-fire.png')
C2_PATH = os.path.join('../assets/images/cards', 'clubs2.gif')
C3_PATH = os.path.join('../assets/images/cards', 'clubs3.gif')
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
FELT_GREEN = (39, 119, 20)

fps = 60
fpsClock = pygame.time.Clock()

# Player card's positions
playerPositionDict = {'pos1' : (200, 463), 'pos2': (280, 463), 'pos3': (360, 463),
                      'pos4' : (440, 463), 'pos5': (520, 463), 'pos6': (600, 463),
                      'pos7' : (680, 463), 'pos8': (760, 463), 'pos9': (840, 463),
                      'pos10': (920, 463)}


# ----------------------------------------------

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        FONT = pygame.font.Font(None, 32)
        self.rect = pygame.Rect(x, y, w, h)
        self.color = GRAY
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        FONT = pygame.font.Font(None, 32)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = RED if self.active else GRAY
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(40, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

# Initialization
pygame.init()
pygame.display.set_icon(icon_surf)
DISPLAYSURF = pygame.display.set_mode((screen_width, screen_height))
DISPLAYSURF.fill(FELT_GREEN) # Background Color
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
    #opponent_card_list = ["diamondsAce", "hearts2", "SpadesKing"] # cards each opponent chose to play
    
    # Opponent 1
    angle = 90
    card = cardGame.card("diamonds", 14)
    card.updateCardPosition(439, 275)
    new_card = pygame.transform.rotate(card.displayCard(), angle)
    DISPLAYSURF.blit(new_card, (card.posx, card.posy))
    
    # Opponent 2
    angle = 180
    card = cardGame.card("hearts", 2)
    card.updateCardPosition(560, 202)
    new_card = pygame.transform.rotate(card.displayCard(), angle)
    DISPLAYSURF.blit(new_card, (card.posx, card.posy))
    
    # Opponent 3
    angle = 90
    card = cardGame.card("spades", 13)
    card.updateCardPosition(657, 275)
    new_card = pygame.transform.rotate(card.displayCard(), angle)
    DISPLAYSURF.blit(new_card, (card.posx, card.posy))
    
    
def trump_card(card_image):
    newLabel("", 845, 40, 83, 107, RED)
    newLabel("Trump Suit", 820, 152, 140, 30, RED)
    DISPLAYSURF.blit(card_image, (850, 45))
    
def card_button(card, position, index, action=None):
    #card.updateCardPosition(198, 461) #Update card's position 
    card.updateCardPosition(playerPositionDict.get(position))
    w =  77
    h = 101
    x = card.posx-2
    y = card.posy-2
    pygame.draw.rect(DISPLAYSURF, BEIGE, (x , y , w , h)) # display button frame

    mouse = pygame.mouse.get_pos() # Get mouse's location
    click = pygame.mouse.get_pressed() # Get mouse click
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF, BRIGHT_RED, (x, y, w, h))
        if click[0] == 1 and action != None:
            if(checkValidity(card, index)):
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
    DISPLAYSURF.blit(card.displayCard(), (560, 323))
    fieldObj.addCard(player1.discard(card.getCard()))
    global playerTurn
    global doneWithTurn
    doneWithTurn = True
    playerTurn = 'p2'
    time.sleep(0.25)
    
def clean_field_action():
    pygame.draw.rect(DISPLAYSURF, FELT_GREEN, (439 , 202, 315, 218))
        
def quit_action():
    pygame.draw.rect(DISPLAYSURF, GRAY, (439 , 202, 315, 218))
    
def next_action():
    global playerTurn
    global waiting
    if(playerTurn == 'p1'):
        playerTurn = 'p2'
    elif(playerTurn == 'p2'):
        playerTurn = 'p3'
    elif(playerTurn == 'p3'):
        playerTurn = 'p4'
    elif(playerTurn == 'p4'):
        playerTurn = 'p1'
    waiting = False
    time.sleep(0.25)
# -----------------------------------------------------
#GLOBALS
#-----------------------------------------------------------------------------
deckObj = cardGame.deck()
fieldObj = cardGame.deck()
player1 = cardGame.player("p1")
comPlayer2 = cardGame.player("p2")
comPlayer3 = cardGame.player("p3")
comPlayer4 = cardGame.player("p4")
suitAsked = None
roundNum = 1
cardsNum = 10
trump = None
GAMEOVER = False

'''IMPORTANT GAME FLOW GLOBALS'''
roundInProgress = False
firstTrickOfRound = True
roundStarter = "p2"     #Player2 starts round 1
trickStarter = "p2"     #keeps track of who starts the next trick
playerTurn = "p2"       #Whoose turn is it currently
doneWithTurn = False    #For p1 only!!
waiting = False         #After computer finish turn wait for NEXT ACTION
#*****************************************************************************
#MAIN
#*****************************************************************************
def main():    
    #CREATE DECK
    for val in range(2, 15):  
        deckObj.addCard(cardGame.card("hearts", val))
    for val in range(2, 15):  
        deckObj.addCard(cardGame.card("diamonds", val))
    for val in range(2, 15):  
        deckObj.addCard(cardGame.card("clubs", val))    
    for val in range(2, 15):
        deckObj.addCard(cardGame.card("spades", val))
        
    bid_input_box = InputBox(640, 640, 40, 40) # note make 600 -> 720
    input_boxes = [bid_input_box]    

    #playerTurnThread = threading.Thread(target=playerTurn, args=(player1,))
    
    #MAIN GAME LOOP
    while (not GAMEOVER):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                exit()
            for box in input_boxes:
                box.handle_event(event)

    
        '''ROUND NOT IN PROGRESS '''
        global roundInProgress
        if(not roundInProgress):
            print("SETTING UP ROUND")
            #Shuffle deck
            deckObj.shuffle()    
            #Deal cards
            try:
                for i in range(cardsNum):
                    player1.addCardToHand(deckObj.drawCard())
                    comPlayer2.addCardToHand(deckObj.drawCard())
                    comPlayer3.addCardToHand(deckObj.drawCard())
                    comPlayer4.addCardToHand(deckObj.drawCard())
            except IndexError:
                pass
            #Choose Trump
            trumpCard = random.choice(deckObj.mydeck)
            
            #TODO
            #set up bidding system
            
            #Setup complete! Round now in progress
            roundInProgress = True
        
        '''ROUND IN PROGRESS '''
        if(roundInProgress):
            '''FIRST TRICK OF ROUND'''
            global firstTrickOfRound
            if(firstTrickOfRound):
                
                global roundStarter
                if(roundStarter == 'p1'):
                    playTrick(roundStarter)
                elif(roundStarter == 'p2'):
                    playTrick(roundStarter)
                elif(roundStarter == 'p3'):
                    playTrick(roundStarter)
                elif(roundStarter == 'p4'):
                    playTrick(roundStarter)
            else: #Not first trick of round
                global trickStarter
                if(trickStarter == 'p1'):
                    playTrick(trickStarter)
                elif(trickStarter == 'p2'):
                    playTrick(trickStarter)
                elif(trickStarter == 'p3'):
                    playTrick(trickStarter)
                elif(trickStarter == 'p4'):
                    playTrick(trickStarter)
            
            # Displaying cards in hand
            showHand()
            if(playerTurn != 'p1'):
                newButton("NEXT", 1025, 490, 90, 50, BLUE, RED, action=next_action)
            else:
                newLabel("", 1025, 490, 90, 50, FELT_GREEN, FELT_GREEN)
                
        
        # Opponent's hands
        opponent_cards(1, 10)
        opponent_cards(2, 10)
        opponent_cards(3, 10)
        
        # Opponent take their turn
        #opponent_play()
        
        # Trump Card
        trump_card(trumpCard.displayCard())
        
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
        newLabel("Your Bid:", 520, 640, 120, 50, BLACK, RED)
        for box in input_boxes:
            box.update()
        for box in input_boxes:
            box.draw(DISPLAYSURF)
        
        fpsClock.tick(60)
        pygame.display.update()
#*****************************************************************************    
                 
if __name__ == '__main__':
    main()
    exit()    
    
    
    
    
    
    
    
    
    
    
    
    