#! /usr/bin/env python3
# Brandon Rupp
# CPSC 386-01
# 2022-03-07
# brandonrupp@csu.fullerton.edu
# @brupp34
#
# Lab 02-00
#
# This is the main file that will be ran for a Pig game
# program that can be played with up to 4 players
#


"""This file runs the entire game through the
directory/package named piggame"""

from piggame import game

if __name__ == '__main__':
    GAME = game.PigGame()
    GAME.run()