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
        
    def outputCard(self):
        print(self.cardName)
        
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
    
    def outputDeck(self):
        for i in self.mydeck:
            print(i.outputCard())