# Brandon Rupp
# CPSC 386-01
# 2022-03-07
# brandonrupp@csu.fullerton.edu
# @brupp34
#
# Lab 02-00
#
# This is the dice file for the Pig game program
#


"""This file rolls the dice for the game outputting a number between 1-6"""


from random import randrange


class Die:
    "Class Die used in game.py"

    def useless(self):
        "Does nothing. Used to pass pylint. I suppose it isn't useless then..."

    @staticmethod
    def roll():
        "Rolls the die returning an int between 1-6"
        return randrange(1, 7)