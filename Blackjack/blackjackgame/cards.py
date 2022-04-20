# Brandon Rupp
# CPSC 386-01
# 2022-03-15
# brandonrupp@csu.fullerton.edu
# @brupp34
#
# Lab 03-00
#
# This is the cards file that conatins the deck of cards
# and that will be ran for a Blackjack program.
#


"""This file contains logic for a deck of cards"""

from collections import namedtuple
from random import shuffle, randrange
from math import floor

Card = namedtuple('Card', ['rank', 'suit'])


class Deck:
    "Deck class that contains a Deck of playing cards"
    Card = namedtuple('Card', ['rank', 'suit'])
    ranks = ['A'] + [str(x) for x in range(2, 11)] + \
        'J Q K'.split()
    suits = '\u2663 \u2665 \u2660 \u2666'.split()
    values = [11] + list(range(2, 11)) + [10, 10, 10]
    value_dict = dict(zip(ranks, values))
    cut_card_position = randrange(60, 81)

    def __init__(self):
        "Initialize the class"
        self._cards = [Card(rank, suit)
            for suit in self.suits for rank in self.ranks]

    def __getitem__(self, position):
        "Getter for item"
        return self._cards[position]

    def __len__(self):
        "Returns length of cards"
        return len(self._cards)

    def shuffle(self, num_shuffles=1):
        "Shuffles the cards n times"
        for _ in range(num_shuffles):
            shuffle(self._cards)

    def cut(self):
        "Cuts the cards"
        cutpos = floor(len(self._cards) * .2)
        half = (len(self._cards) // 2) + \
            randrange(-cutpos, cutpos) # 2 shalshes means int math
        tophalf = self._cards[:half]
        bottomhalf = self._cards[half:]
        self._cards = bottomhalf + tophalf

    def __str__(self):
        "Joins the cards together in a string"
        return '\n'.join(map(str, self._cards))

    def deal(self):
        "Deals the cards"
        return self._cards.pop(0)

    def needs_shuffling(self):
        "Checks to see if the cards need to be shuffled"
        if len(self._cards) <= ((52*8) - self.cut_card_position):
            return True
        return False

    def merge(self, other_deck):
        """Merge the current deck with the deck passed as a parameter."""
        self._cards = self._cards + other_deck._cards

    def card_value(card):
        """Return the numerical value of the rank of a given card."""
        return Deck.value_dict[card.rank]