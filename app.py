import random

SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUES = {'2': 2, '3': 3, '4': 4, "5": 5,
          '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[self.rank]

    def __str__(self):
        return self.rank + ' of '+self.suit + ' with value ' + str(self.value)


class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)
        random.shuffle(self.cards)


my_deck = Deck()
for card in my_deck.cards:
    print(card)
    print(f'\t{card.value}')
