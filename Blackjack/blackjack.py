#!/usr/bin/env python3
# Brandon Rupp
# CPSC 386-01
# 2022-03-15
# brandonrupp@csu.fullerton.edu
# @brupp34
#
# Lab 03-00
#
# This is the main file that will be ran for a Blackjack
# program.
#


"""This file runs the entire game through the
directory/package named blackjackgame"""

from blackjackgame import game

if __name__ == '__main__':
    GAME = game.BlackJack()
    GAME.run()