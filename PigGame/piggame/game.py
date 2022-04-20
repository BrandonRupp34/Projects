# Brandon Rupp
# CPSC 386-01
# 2022-03-07
# brandonrupp@csu.fullerton.edu
# @brupp34
#
# Lab 02-00
#
# This is the game file for the Pig game program
#


"""Contains all of the logic for Pig game"""


import array as arr
from time import sleep
from .dice import Die
from .player import Player, ComputerPlayer


class PigGame:
    """Main class for Pig game that contains all of the logic"""
    def __init__(self):
        "Initialize the players"
        self._players = []

    def run(self):
        "Runs the game"
        dieroll = Die()
        print("Welcome to Pig Game!\n")
        sleep(0.5)
        num_players = int(input("How many players? [1-4] "))
        for i in range(num_players):
            name = input("What is player {}'s name? ".format(i + 1))
            order = dieroll.roll()
            print("Rolling for turn order")
            sleep(0.5)
            print("You rolled {}.\n".format(order))
            sleep(0.5)
            self._players.append(Player(name, order))
        if num_players == 1:
            order = dieroll.roll()
            self._players.append(ComputerPlayer(order, self))
        print("Before sorting ", self._players)
        sleep(1)
        self._players.sort(key=lambda p: p.order, reverse=True)
        print("After sorting ", self._players)
        sleep(1)
        current_player_index = 0
        gameover = False
        cpscore = arr.array("i", [0, 0, 0, 0, 0])
        while gameover is False:
            currplayer = self._players[current_player_index]
            round_score = cpscore[current_player_index]
            print("\n{} is up!".format(currplayer))
            sleep(1)
            playerroll = "y"
            rolled_number = 5
            rolls = 1
            current_score = 0
            if currplayer.am_i_human():
                while (
                    playerroll.lower() != ("n")
                    and rolled_number != 1
                    and gameover is False
                ):
                    if Player.does_roll(playerroll):
                        rolled_number = dieroll.roll()
                        print("You rolled {}".format(rolled_number))
                        if rolled_number != 1:
                            current_score = Player.round_score(
                                rolled_number, round_score
                            )
                            round_score = current_score
                            print("Total score: {} ".format(current_score))
                        else:
                            print("You lost your turn!")
                    if rolled_number != 1:
                        if current_score >= 30:
                            gameover = True
                        else:
                            playerroll = input("Roll again? (Y/N) ")
                        if playerroll.lower() == "y":
                            print("")
                    if playerroll.lower() == ("n"):
                        print("{} is ending their turn.".format(currplayer))
                        cpscore[current_player_index] = current_score
            if not currplayer.am_i_human():
                while (
                    ComputerPlayer.does_comp_roll(rolls)
                    and rolled_number != 1
                    and gameover is False
                ):
                    rolls = ComputerPlayer.roll_counter(rolls)
                    rolled_number = dieroll.roll()
                    print("{} rolled {}".format(currplayer, rolled_number))
                    if rolled_number != 1:
                        current_score = Player.round_score(rolled_number, round_score)
                        round_score = current_score
                        print("Total score: {} \n".format(current_score))
                        sleep(0.5)
                    else:
                        print("{} lost their turn!".format(currplayer))
                        rolls = 0
                    if rolled_number != 1:
                        if current_score >= 30:
                            gameover = True
                if (not ComputerPlayer.does_comp_roll(rolls) and rolled_number != 1):
                    print("{} is ending their turn.".format(currplayer))
                    rolls = 0
                    cpscore[current_player_index] = current_score
            sleep(1)
            current_player_index = ((current_player_index + 1) % len(self._players))
        print(
            "\nGame Over! \n{} is the winner!"
            "\nThanks for playing Pig Game! :)".format(currplayer)
        )
