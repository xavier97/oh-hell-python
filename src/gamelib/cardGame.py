# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 11:58:48 2019

@author: Nicholas
"""
import random

class card:
    def __init__(self, s, val):
        if(val < 11):
            name = s + str(val)
        elif(val == 11):
            name = s + "Jack"
        elif(val == 12):
            name = s + "Queen"
        elif(val == 13):
            name = s + "King"
        elif(val == 14):
            name = s + "Ace"
        self.cardName = name
        self.suit = s
        self.value = val
        
    def getCard(self):
        return self.cardName
    
    def getSuit(self):
        return self.suit
    
    def getVal(self):
        return self.value
        
class deck:
    def __init__(self):
        self.mydeck = []
        
    def addCard(self, card):
        self.mydeck.append(card)
        
    def shuffle(self):
        random.shuffle(self.mydeck)
        
    def drawCard(self):
        card = self.mydeck[0]
        del self.mydeck[0]
        return card
    
    def toStringDeck(self):
        for i in self.mydeck:
            return i.getCard()
            
class player:
    def __init__(self):
        self.hand = []
        self.bid = 0
        self.tricks = 0
        self.points = 0
        
    def setBid(self, b):
        self.bid = b
        
    def getBid(self):
        return self.bid
    
    def addTrick(self, t):
        self.tricks = self.tricks + t
        
    def clearTricks(self):
        self.tricks = 0
        
    def getTricks(self):
        return self.tricks
    
    def calcPoints(self, points, add):
        if(add):
            self.points += points
        else:
            self.points -= points
            
    def getPoints(self):
        return self.points
    
    def clearPoints(self):
        self.points = 0
        
    def addCardToHand(self, card):
        self.hand.append(card)
        
    def discard(self, index):
        card = self.hand[index]
        del self.hand[index]
        return card