# Brandon Rupp
# CPSC 386-01
# 2022-03-07
# brandonrupp@csu.fullerton.edu
# @brupp34
#
# Lab 02-00
#
# This is the Player file for pig game
#


"""This file contains the player order, player roll logic, and AI logic"""


class Player:
    "This class conatins all the logic for the player"
    def __init__(self, name, order):
        "Initializes the name, turn order, and score for the players"
        self._name = name
        self._order = order
        self._score = 0

    @property
    def name(self):
        "Returns name"
        return self._name

    @property
    def order(self):
        "Returns player order"
        return self._order

    @property
    def score(self):
        "Returns player score"
        return self._score

    @staticmethod
    def round_score(rolled_score, curr_score):
        "Adds the score rolled on the die to the total score for the round"
        curr_score += rolled_score
        return curr_score

    @staticmethod
    def does_roll(answer):
        "Checks to see if the player wants to roll again"
        if answer.lower() == ("y"):
            return True
        return False

    @staticmethod
    def am_i_human():
        "Checks if player is a computer or player"
        return True

    def __str__(self):
        "Returns player name"
        return self._name

    def __repr__(self):
        "Returns player with the initial number rolled to determine the order"
        return 'Player("{}", {})'.format(self._name, self._order)


class ComputerPlayer(Player):
    "A subclass of player that contains the logic for the computer player"
    def __init__(self, order, game):
        "Initializes the computer player"
        super().__init__("Sonny", order)
        self._game = game

    def am_i_human(self):
        "Checks to see if player is computer"
        return False

    @staticmethod
    def roll_counter(counter):
        "Adds 1 to the passed in variable, acting as a counter"
        counter += 1
        return counter

    @staticmethod
    def does_comp_roll(roll):
        "Checks to see if the computer is going to roll again on their turn"
        if roll % 4 == 0:  # Computer rolls 3 times then stops
            return False
        roll = 0
        return True
