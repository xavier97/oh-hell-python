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
        self.tagID = 0
        
    def getCard(self):
        return self.cardName
    
    def getSuit(self):
        return self.suit
    
    def getVal(self):
        return self.value
    
    #Keep track of who played the card
    def setTagID(self, ID):
        self.playerID = ID
        
    def getTagID(self):
        return self.playerID
        
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
    
    def flipCard(self):
        return self.mydeck[0].getCard()
    
    def toStringDeck(self):
        decklist = []
        for i in self.mydeck:
            decklist.append(i.getCard())
        return print(decklist)
            
class player:
    def __init__(self, ID):
        self.hand = []
        self.bid = 0
        self.tricks = 0
        self.points = 0
        self.playerID = ID
        
    def getPlayerID(self):
        return self.playerID
        
    def setBid(self, b):
        self.bid = b
        
    def getBid(self):
        return self.bid
    
    def addTrick(self):
        self.tricks = self.tricks + 1
        
    def clearTricks(self):
        self.tricks = 0
        
    def getTricks(self):
        return self.tricks
    
    def addPoints(self, points):
        self.points += points
            
    def getPoints(self):
        return self.points
    
    def clearPoints(self):
        self.points = 0
    
    #Checks the validity of a play
    def checkPlay(self, index, suitAsked):
        if(self.hand[index].getSuit() == suitAsked):
            return True
        else:
            for card in self.hand:
                if(card.getSuit() == suitAsked):
                    return False
            return True
            
    def addCardToHand(self, card):
        card.setTagID(self.playerID)
        self.hand.append(card)
    
    def viewHand(self):
        handString = ""
        for index in range(len(self.hand)):
            handString = handString + str(index) + ")" + str(self.hand[index].getCard()) + " | "
        return print(handString)

    #Discards suit asked if suit is in hand. Else discards a random card
    def discardBySuit(self, suitAsked):
        for index in range(len(self.hand)):
            if(self.hand[index].getSuit() == suitAsked):
                return self.discard(index)
        return self.discard(random.choice(range(len(self.hand))))            
    
    #Discards specified card         
    def discard(self, index):
        card = self.hand[index]
        del self.hand[index]
        return card 