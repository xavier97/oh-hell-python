# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:34:47 2019

@author: Nicholas
"""
from gamelib import cardGame
import random

def computerTurn(comp):
    global fieldObj
    global suitAsked
    if(not fieldObj.mydeck):
        cardPlayed = comp.discard(random.choice(range(len(comp.hand))))
        fieldObj.addCard(cardPlayed)
        suitAsked = cardPlayed.getSuit()
    else:
        cardPlayed = comp.discardBySuit(suitAsked)
        fieldObj.addCard(cardPlayed)
        

#GLOBALS
#-----------------------------------------------------------------------------
deckObj = cardGame.deck()
fieldObj = cardGame.deck()
player1 = cardGame.player()
comPlayer2 = cardGame.player()
comPlayer3 = cardGame.player()
comPlayer4 = cardGame.player()
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

'''
cardlist = []
handList = []
for i in range(1,6):
    handList.append(deckObj.drawCard().getCard())
    
for i in deckObj.mydeck:
    cardlist.append(i.getCard())
'''    

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
    
#Computer Turns
computerTurn(comPlayer2)
computerTurn(comPlayer3)
computerTurn(comPlayer4)

print("\nFIELD: \n---------------------------------")
fieldObj.toStringDeck()
print("Suit asked: " + suitAsked.upper())
print("Trump: " + trump.upper())
print("---------------------------------")

print("\n YOUR HAND:")
player1.viewHand()






       
    

































