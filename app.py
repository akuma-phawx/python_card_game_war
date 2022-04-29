'''
    The War Card Game!
'''
from ast import arguments
from random import shuffle

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


class Player:

    def __init__(self, name):
        self.name = name
        self.card_list = []


class Deck:

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        '''
            Creates the deck for the players to play.
        '''
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.cards.append(card)

        print(f'Deck was created with {len(self.cards)} cards.\n')

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, *args):
        self.hands = [self.cards[i::len(args)]
                      for i in range(0, len(args))]
        try:
            args[0].cards = self.hands[0]
            args[1].cards = self.hands[1]
        except:
            print('Not enough players')


def introduction():
    '''
        Prints the rules of the game.
    '''
    print('\nWelcome to War! The player who is out of card loses !')
    print('\t-Both players start with a deck of 26 cards')
    print("\t-Both players draw a card. If your card's value is bigger than your opponent you put the card in your deck")
    print('\t-If the value is the same you draw another and the winner gets all the cards')
    print('\t-The player with 0 cards left loses!')
    print('\n---------\n')


def start_game(deck, p1, p2):
    print(f'Starting the game! {p1.name} vs {p2.name}! Fight!')


introduction()
my_deck = Deck()
my_deck.shuffle()

p1 = Player('Nick')
p2 = Player('Bob')

my_deck.deal(p1, p2)

start_game(my_deck, p1, p2)
