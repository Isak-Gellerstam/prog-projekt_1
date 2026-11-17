import random

from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    
    @staticmethod
    def make_deck(self):
        self.cards = []
        colors = ["red", "blue", "green", "yellow"]

        for color in colors:
            for number in range(10):
                for _ in range(2):
                    self.cards.append(Card(color, str(number)))

                    