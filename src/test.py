# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:34:47 2019

@author: Nicholas
"""
from gamelib import cardGame
import random

#GAMEPLAY FUNCTIONS
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
    
def playTrick():
    if(startingPlayer == "p1"):
        print("You play first! Pick any card to start the trick")
        showHand()
        playerTurn(player1)
        computerTurn(comPlayer2)
        computerTurn(comPlayer3)
        computerTurn(comPlayer4)
    elif(startingPlayer == "p2"):
        print("Player 2 starts the trick")
        computerTurn(comPlayer2)
        computerTurn(comPlayer3)
        computerTurn(comPlayer4)
        viewField()
        showHand()
        playerTurn(player1)
    elif(startingPlayer == "p3"):
        print("Player 3 starts the trick")
        computerTurn(comPlayer3)
        computerTurn(comPlayer4)
        viewField()
        showHand()
        playerTurn(player1)
        computerTurn(comPlayer2)
    elif(startingPlayer == "p4"):
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
        print("LOOP LOOP LOOP")
        #If card is trump
        if(card.getSuit() == trump):
            #If current winning card isn't trump automatic win
            if(winningSuit == suitAsked):
                winningCard = card
                winningSuit = trump
                winningVal = card.getVal()
            #If current winning card is also trump check values 
            elif(card.getVal() > winningVal):
                winningCard = card
        #If card is suit asked
        elif(card.getSuit() == suitAsked):
            if((winningSuit != trump) and (card.getVal() > winningVal)):
                winningCard = card
                winningVal = card.getVal()
        print("Winning val: " + str(winningVal))
                
    print("WINNING CARD: " + winningCard.getCard())
   
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
    global startingPlayer 
    startingPlayer = winningCard.getTagID()
    print("*** " + startingPlayer + " won the trick! ***")
    print("END OF TRICK")
    print("---------------------------------")
    #Reset suitAsked
    suitAsked = None
    
#TODO 
#ResolveRound
#-----------------------------------------------------------------------------       
        
#GLOBALS
#-----------------------------------------------------------------------------
deckObj = cardGame.deck()
fieldObj = cardGame.deck()
player1 = cardGame.player("p1")
comPlayer2 = cardGame.player("p2")
comPlayer3 = cardGame.player("p3")
comPlayer4 = cardGame.player("p4")
startingPlayer = "p2"  #Player2 starts round 1
suitAsked = None
roundNum = 1
cardsNum = 13
trump = None
done = False
#-----------------------------------------------------------------------------

for val in range(2, 15):  
    deckObj.addCard(cardGame.card("hearts", val))
for val in range(2, 15):  
    deckObj.addCard(cardGame.card("diamonds", val))
for val in range(2, 15):  
    deckObj.addCard(cardGame.card("clubs", val))    
for val in range(2, 15):
    deckObj.addCard(cardGame.card("spades", val))

print("Deck created")
deckObj.toStringDeck()
deckObj.shuffle()

print("Welcome to Oh Hell!")
#GAME LOOP
'''
while(not done):
    print("Starting Round " + str(roundNum))
    if(roundNum < 13):
        print("Dealing every player " + str(cardsNum) + " cards")
    else:
        print("Dealing every player " + str(cardsNum) + " card")
        
    for i in range(cardsNum):
        player1.addCardToHand(deckObj.drawCard())
        comPlayer2.addCardToHand(deckObj.drawCard())
        comPlayer3.addCardToHand(deckObj.drawCard())
        comPlayer4.addCardToHand(deckObj.drawCard())
        
    player1.viewHand()
    
    roundNum += 1;
    cardsNum -= 1;
    if(roundNum > 13):
        done = True
'''

#TEST ROUND
#-----------------------------------------------------------------------------
print("Starting Round " + str(roundNum))
if(roundNum < 13):
    print("Dealing every player " + str(cardsNum) + " cards")
else:
    print("Dealing every player " + str(cardsNum) + " card")

#shuffle deck
deckObj.shuffle()

#Deal cards        
for i in range(cardsNum):
    player1.addCardToHand(deckObj.drawCard())
    comPlayer2.addCardToHand(deckObj.drawCard())
    comPlayer3.addCardToHand(deckObj.drawCard())
    comPlayer4.addCardToHand(deckObj.drawCard())

#Choose trump
if(roundNum == 1):
    suits = ["hearts", "spades","diamonds","clubs"]
    trump = random.choice(suits)
else:
    trump = random.choice(deckObj.mydeck).getSuit()

print("Trump this round: " + trump.upper())

print("\n YOUR HAND:")
player1.viewHand()

#Bidding
while(True):
    bid = int(input("\nEnter your bid: "))
    if((bid >= 0) and (bid <= cardsNum)):
        break
    else:
        print("Error: Please enter bid between 0 and " + str(cardsNum))
player1.setBid(bid)
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
    
playTrick()
viewField()
resolveTrick()
playTrick()
viewField()
resolveTrick()






       
    






















