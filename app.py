'''
    The War Card Game!
'''
from multiprocessing.sharedctypes import Value
from random import shuffle

SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALUES = {'2': 2, '3': 3, '4': 4, "5": 5,
          '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


class Card:
    '''
        Card blueprint
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[self.rank]

    def __str__(self):
        return self.rank + ' of '+self.suit + '.'


class Player:
    '''
        Player blueprint
    '''

    def __init__(self, name):
        self.name = name
        self.card_list = []
        self.hands = []
        print(
            f"Player {self.name} was created.")

    def __str__(self):
        return self.name + ' has ' + str(len(self.card_list)) + ' remaining cards.'

    def add_cards(self, new_cards):
        '''
            Adds cards in players card list.
        '''
        self.card_list.extend(new_cards)

    def draw_card(self):
        '''
            Draws the first card in the list.
        '''
        return self.card_list.pop(0)


class Deck:
    '''
        Deck blueprint and functionality
    '''

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
        '''
            Shuffles the deck.
        '''
        shuffle(self.cards)
        print('Deck shuffled.\n')

    def deal(self, number_of_players):
        '''
            Deals the cards to the players
        '''
        self.hands = [self.cards[i::number_of_players]
                      for i in range(0, number_of_players)]

        print('Deck dealed.')
        return tuple(self.hands)


def introduction():
    '''
        Prints the rules of the game.
    '''
    print('\nWelcome to War! The player who is out of card loses !')
    print('\t-Both players start with a deck of 26 cards')
    print("\t-Both players draw a card. Highest value wins.")
    print('\t-If the value is the same you draw another and the winner gets all the cards')
    print('\t-The player with 0 cards left loses!')
    print('\n---------\n')


def print_game_menu():
    '''
        Prints the game menu.
    '''
    print('Game Menu:\n\t(1) Draw Cards.\n\t(2) Show remaining cards.\n\t(3) Quit Game.\n')


def compare_values(card_one, card_two):
    '''
        Compares the values of 2 given cards.
        If negative return card two gwins if possitive card one wins if 0 draw.
    '''
    return card_one.value - card_two.value


def check_for_winner(p1_cards, p2_cards):
    '''
        Checks if theres a winner and who is the winner
        Returns a tuple of structure (game is over, winner string)
    '''

    if p1_cards == 0:
        return (True, 'Player 2')
    elif p2_cards == 0:
        return (True, 'Player 1')
    else:
        return (False, None)


def start_game(deck, player_one, player_two):
    '''
       Starts the game
    '''
    game_over = False
    winner = None
    stash = []

    print(f'Starting the game! {player_one.name} vs {player_two.name}! Fight!')
    while not game_over:
        print_game_menu()
        user_input = input('Your choice: ')
        try:
            if(int(user_input) < 1 or int(user_input) > 3):
                print('\nNot a valid choice. Try again.\n')
            else:
                if(user_input == '1'):
                    player_one_drawn_card = player_one.draw_card()
                    player_two_drawn_card = player_two.draw_card()
                    print(
                        f'\tP1 [{player_one.name}] draw : {player_one_drawn_card}')
                    print(
                        f'\tP1 [{player_two.name}] draw : {player_two_drawn_card}')

                    stash.append(player_one_drawn_card)
                    stash.append(player_two_drawn_card)

                    comparison_result = compare_values(player_one_drawn_card,
                                                       player_two_drawn_card)
                    if(comparison_result > 0):
                        print('Player One wins!\n')
                        player_one.add_cards(stash)
                        stash = []
                    elif(comparison_result < 0):
                        print('Player Two wins!\n')
                        player_two.add_cards(stash)
                        stash = []
                    else:
                        print(
                            f'Cards added in the stash. We are at War!\n Cards in stash: {len(stash)} ')

                    game_over, winner = check_for_winner(
                        len(player_one.card_list), len(player_two.card_list))
                elif(user_input == '2'):
                    print('\n', player_one, '\n')
                    print('\n', player_two, '\n')
                    print('\n', f'Cards in stash {len(stash)}', '\n')
                else:
                    exit()
        except ValueError or TypeError:
            print('\nNot a valid choice. Try again.\n')
            continue
    print(f'Congratulations {winner} - You won!!')


if __name__ == "__main__":
    introduction()

    my_deck = Deck()
    my_deck.shuffle()

    player_one = Player('Nick')
    player_two = Player('Bob')
    player_one.card_list, player_two.card_list = my_deck.deal(2)

    start_game(my_deck, player_one, player_two)
