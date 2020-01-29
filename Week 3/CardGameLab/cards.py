from random import shuffle

"""Defines the following classes; Card, Deck, PlayerHand
Designed specifically to support the game WAR
"""
ranks = [str(n) for n in range(2, 11)] + 'Jack Queen King Ace'.split()
suits = 'Spades Diamonds Clubs Hearts'.split()
face_values = {'Jack': 11,
               'Queen': 12,
               'King': 13,
               'Ace': 14}


class Card:
    """Defines a card class for use in card games

    """

    def value(self):
        """Value is specific to the game of war for comparing cards

        :return: (int) ranked value of the card
        """
        if self.rank.isnumeric():
            return int(self.rank)
        return face_values[self.rank]

    def __init__(self, rank, suit):
        """Initialize a new card

        :param rank: (str) Must be in Card.ranks
        :param suit: (str) Must be in Card.suits
        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        """Initialize a new deck"""

        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def draw_card(self):
        """Draws the top card of the deck.

        :return: (Card) Top card of deck
        """
        return self.cards.pop(0)

    def shuffle(self):
        """Shuffles the deck"""

        shuffle(self.cards)


class Player:

    def __init__(self, name):
        """Initalize a new player
        :param name: (str) The name of the player.
        """
        self.name = name
        self.cards = []

    def __str__(self):
        return f'{self.name}'

    def add_cards_to_bottom(self, cards):
        """Adds cards to the bottom of the player's personal hand"""
        self.cards.extend(card)

    def draw_from_top(self):
        """Draws the top card off the player's hand

        :return: (Card) Top card of player's hand
        """
        return self.cards.pop(0)
