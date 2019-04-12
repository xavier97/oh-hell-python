# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:34:47 2019

@author: Nicholas
"""
from gamelib import cardGame

deckObj = cardGame.deck()

for val in range(2, 15):  
    deckObj.addCard(cardGame.card("hearts", val))
for val in range(2, 15):  
    deckObj.addCard(cardGame.card("diamonds", val))
for val in range(2, 15):  
    deckObj.addCard(cardGame.card("clubs", val))    
for val in range(2, 15):
    deckObj.addCard(cardGame.card("spades", val))

mylist = []
cardlist = []
mylist = deckObj.mydeck

for i in mylist:
    cardlist.append(i.outputCard())
    
deckObj.shuffle()
print(deckObj.drawCard().outputCard())

#print(len(deckObj.mydeck))
#print(deckObj.outputDeck())