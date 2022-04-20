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


"""This file has all of the game logic for the blackjack program"""

from .cards import Deck
from time import sleep
from .player import Player, Dealer
import pickle


class BlackJack:
    "Main class for BlackJack that contains all of the logic"
    def setup(self):
        "Initializes the game"
        self._players = []
        try:
            self._players = self.from_file('players.pckl')
        except FileNotFoundError:
            pass
        index = []
        print("Welcome to BlackJack!\n")
        num_players = int(input("How many players? [1-4] "))
        for i in range(num_players):
            name = input("What is player {}'s name? ".format(i+1))
            new_player = True
            new_dealer = True
            for x in range(len(self._players)):
                if name == Player.get_name(self._players[x]):
                    print(f"Welcome back {name}")
                    index.append(x)
                    new_player = False
            if (new_player):
                self._players.append(Player(name))
                index.append(len(self._players)- 1)
        for y in range(len(self._players)):
            if Player.get_name(self._players[y]) == "Dealer":
                index.append(y)
                new_dealer = False
        if (new_dealer):
            self._players.append(Dealer("Dealer"))
            index.append(len(self._players) - 1)
        return index

    def run(self):
        "Runs the game"
        current_player_index = 0
        currdeck = self.newdeck()
        keep_playing = True
        index = self.setup()
        dealer_bj = False
        insurance = False
        while keep_playing is True:
            currplayer = self._players[index[current_player_index]]
            for i in range(len(index)):
                if currplayer.am_i_human():
                    if (Player.get_balance(currplayer) <= 0):
                        Player.set_balance(currplayer, 10000)
                        print("{} got an anoynmos donation of $10,000".format\
                            (Player.get_name(currplayer)))
                current_player_index = \
                    self.curr_player_index_plus(current_player_index, index)
                currplayer = self.next_player(currplayer, current_player_index,\
                    index)
            if (Deck.needs_shuffling(currdeck)):
                currdeck = self.newdeck()
            # Asks the players how much they would like to bet and then stores
            # it their player class
            for i in range(len(index)):
                if currplayer.am_i_human():
                    self.hand_bets(currplayer)
                current_player_index = \
                    self.curr_player_index_plus(current_player_index, index)
                currplayer = self.next_player(currplayer, current_player_index,\
                    index)
            # Deals the initial 2 cards to the players and dealer
            for x in range(2):
                for i in range(len(index)):
                    Player.set_hand(currplayer, Deck.deal(currdeck))
                    Player.set_num_cards(currplayer, 2)
                    if Player.get_hand(currplayer, x).rank == 'A':
                        Player.set_ace_index(currplayer, i)
                    current_player_index = \
                        self.curr_player_index_plus(current_player_index, index)
                    currplayer = self.next_player(currplayer, current_player_index\
                        , index)
            for i in range(len(index)):
                # Prints out every players cards along with their score,
                # excluding the dealer's second card
                Player.set_hand_score(currplayer,\
                    (Deck.card_value(Player.get_hand(currplayer, 0)) + \
                        (Deck.card_value(Player.get_hand(currplayer, 1)))))
                if currplayer.am_i_human():
                    print("{}'s hand: {}{} {}{}".format(Player.get_name(currplayer),\
                        Player.get_hand(currplayer, 0).rank,\
                            Player.get_hand(currplayer, 0).suit,\
                                Player.get_hand(currplayer, 1).rank,\
                                    Player.get_hand(currplayer, 1).suit))
                    print("{}'s hand score: {}\n".format\
                        (Player.get_name(currplayer),\
                            Player.get_hand_score(currplayer)))
                else:
                    dealer = currplayer
                    print("{}'s hand: {}{} XX".format(Player.get_name(currplayer), \
                        Player.get_hand(currplayer, 0).rank,\
                            Player.get_hand(currplayer,0).suit))
                    dealer_card = Deck.card_value(Player.get_hand(currplayer, 0))
                    print("Dealer showing: {}\n".format(dealer_card))
                current_player_index = \
                    self.curr_player_index_plus(current_player_index, index)
                currplayer = self.next_player(currplayer, current_player_index,\
                    index)
            for i in range(len(index)):
                # Checks for insurance and blackjacks
                Player.set_black_jack(currplayer, self.check_blackjack(currplayer))
                if ((currplayer.am_i_human()) and\
                    (Player.get_black_jack(currplayer) is True)):
                        Player.set_stand(currplayer, True)
                        print("{} got blackjack!\n".format\
                            (Player.get_name(currplayer)))
                        if len(index) == 2:
                            Dealer.set_stand(dealer, True)
                if currplayer.am_i_human():
                    insurance = self.check_insurance(currplayer, dealer_card)
                    if insurance:
                        self.insurance(currplayer)
                if ((currplayer.am_i_human() is False) and \
                    (Player.get_black_jack(currplayer) is False) and \
                        (insurance is True)):
                            dealer_bj = False
                            print("Dealer does not have Blackjack")
                if ((currplayer.am_i_human() is False) and \
                    (Player.get_black_jack(currplayer))):
                        print("Dealer has blackjack")
                        dealer_score = Dealer.get_hand_score(currplayer)
                        dealer_bj = True
                        for y in range(len(index)):
                            Player.set_stand(currplayer, True)
                            current_player_index = self.curr_player_index_plus\
                                (current_player_index, index)
                            currplayer = self.next_player(currplayer, \
                                current_player_index, index)
                current_player_index = self.curr_player_index_plus\
                    (current_player_index, index)
                currplayer = self.next_player(currplayer, \
                    current_player_index, index)
            for i in range(len(index)):
                if currplayer.am_i_human():
                    if (Player.get_stand(currplayer) is False):
                        self.check_split(currplayer, currdeck)
                        if (Player.get_stand(currplayer) is False):
                            userinput = input("{}, Would you like to double down?(Y/N)"\
                                .format(Player.get_name(currplayer)))
                            if self.check_user_input(userinput):
                                Player.set_bet(currplayer, (Player.get_bet(currplayer) *2))
                                self.hit(currplayer, Player.get_num_cards\
                                    (currplayer), currdeck)
                                Player.set_stand(currplayer, True)
                                if Player.bust(currplayer):
                                    print(f"{Player.get_name(currplayer)} bust!\n")
                    userinput = 'y'
                    while(self.check_user_input(userinput) is True \
                        and Player.bust(currplayer) is False and \
                            Player.get_stand(currplayer) is False):
                        userinput = input("{}, Would you like to hit? (Y/N)"\
                            .format(Player.get_name(currplayer)))
                        if self.check_user_input(userinput):
                            self.hit(currplayer, Player.get_num_cards(currplayer),\
                                currdeck)
                            if Player.bust(currplayer) is True:
                                print(f"{Player.get_name(currplayer)} bust!\n")
                        else:
                            Player.set_stand(currplayer, True)
                if currplayer.am_i_human() is False:
                    dealer_score = Dealer.get_hand_score(currplayer)
                    dealer_bust = False
                    if Dealer.does_hit(currplayer, Dealer.get_hand_score\
                        (currplayer) is False):
                        print(Player.get_hand(currplayer, 0).rank,\
                            Player.get_hand(currplayer, 0).suit)
                        print(Player.get_hand(currplayer, 1).rank,\
                            Player.get_hand(currplayer, 1).suit)
                        print("{}'s hand score: {}\n".format\
                            (Player.get_name(currplayer),\
                                Player.get_hand_score(currplayer)))
                    while Dealer.does_hit(currplayer, \
                        Dealer.get_hand_score(currplayer)):
                        self.hit(currplayer, Player.get_num_cards(currplayer),\
                            currdeck)
                        dealer_score = Dealer.get_hand_score(currplayer)
                        if (dealer_score > 21):
                            dealer_bust = True
                            print(f"{Player.get_name(currplayer)} bust!\n")
                current_player_index = \
                    self.curr_player_index_plus(current_player_index, index)
                currplayer = self.next_player(currplayer, current_player_index,\
                    index)
            for i in range(len(index)):
                #Scoring and paying out bets
                if currplayer.am_i_human():
                    if Player.get_insurance(currplayer):
                        if (dealer_bj):
                            Player.win_side_bet(currplayer)
                        else:
                            Player.lose_side_bet(currplayer)
                    if Player.get_split(currplayer):
                        if (((Player.get_split_hand_score(currplayer) < 22) and\
                            (((Player.get_split_hand_score(currplayer) > dealer_score))\
                                or (dealer_bust)))):
                                    Player.win_bet(currplayer)
                        elif (Player.get_split_hand_score(currplayer) == dealer_score) and \
                            (dealer_bust is False):
                            print("Push for {}, no change in balance\n".format(\
                                currplayer.get_name()))
                        else:
                            Player.lose_bet(currplayer)
                    if (((Player.get_hand_score(currplayer) < 22) and\
                        (((Player.get_hand_score(currplayer) > dealer_score))\
                            or (dealer_bust)))):
                                Player.win_bet(currplayer)
                    elif (Player.get_hand_score(currplayer) == dealer_score) and \
                        (dealer_bust is False):
                        print("Push for {}, no change in balance\n".format(\
                            currplayer.get_name()))
                    else:
                        Player.lose_bet(currplayer)
                Player.round_reset(currplayer)
                current_player_index = \
                    self.curr_player_index_plus(current_player_index, index)
                currplayer = self.next_player(currplayer, current_player_index,\
                    index)
            if self.check_user_input(input\
                ("Would you like to play another round? (Y/N)")) is False:
                    keep_playing = False
                    self.to_file('players.pckl', self._players)
                    print("Thanks for playing BlackJack!")

    def check_user_input(self, user_input):
        "Checks user input for y"
        if (user_input.lower() == "y"):
            return True
        return False

    def check_blackjack(self, currplayer):
        "Checks to see if the player has blackjack"
        if int(Player.get_hand_score(currplayer)) == 21:
            return True
        return False

    def check_split(self, currplayer, currdeck):
        "Checks to see if the user can split and ask if they would like to do so"
        if Deck.card_value(Player.get_hand(currplayer, 0)) ==\
            Deck.card_value(Player.get_hand(currplayer, 1)):
                uinput = input("{}, Would you like to split?(Y/N)".format(
                    Player.get_name(currplayer)))
                if (self.check_user_input(uinput)):
                    self.split(currplayer, currdeck)

    def check_insurance(self, currplayer, dealer_card):
        "Checks to see if insurance needs to be offered"
        if currplayer.am_i_human():
            if ((dealer_card == 10) or (dealer_card == 11)):
                return True

    def next_player(self, currplayer, current_player_index, index):
        "Indexs to the next player"
        currplayer = self._players[index[current_player_index]]
        return currplayer

    def hand_bets(self, currplayer):
        "Gets the initial bets for the round"
        print("{}, Your balance is {}".format(Player.get_name(currplayer), \
            Player.get_balance(currplayer)))
        Player.set_bet(currplayer, \
            input("How much would you like to bet on this hand? "))
        print("\n")

    def curr_player_index_plus(self, current_player_index, index = []):
        "Adds 1 to the current player index"
        current_player_index = ((current_player_index + 1) % len(index))
        return current_player_index

    def hit(self, currplayer, numcards, currdeck):
        "Asks the players if they want to hit and then deals them a card"
        Player.set_hand(currplayer, Deck.deal(currdeck))
        for i in range(numcards + 1):
            print(Player.get_hand(currplayer, i).rank, \
                Player.get_hand(currplayer, i).suit)
        Player.set_hand_score(currplayer,\
                ((Deck.card_value(Player.get_hand(currplayer, numcards))) + \
                    (Player.get_hand_score(currplayer))))
        if Player.get_hand(currplayer, numcards).rank == 'A':
            Player.set_ace_index(currplayer, Player.get_num_cards(currplayer))
        Player.bust(currplayer)
        Player.set_num_cards(currplayer, (numcards + 1))
        Player.set_black_jack(currplayer, self.check_blackjack(currplayer))
        print("{}'s hand score: {}\n".format(Player.get_name(currplayer), \
            Player.get_hand_score(currplayer)))
        if ((currplayer.am_i_human()) and\
            (Player.get_black_jack(currplayer) is True)):
                Player.set_stand(currplayer, True)
                print("{} got blackjack!\n".format\
                (Player.get_name(currplayer)))

    def newdeck(self):
        "Creates a new deck of 8 combined decks"
        currdeck = Deck()
        for i in range(7):
            Deck.merge(currdeck, Deck())
        Deck.shuffle(currdeck, 10)
        Deck.cut(currdeck)
        print("Creating new deck...")
        return currdeck

    def split(self, currplayer, currdeck):
        "Splits the players hand after they are able"
        Player.set_split_hand(currplayer, Player.pop_player_card(currplayer))
        Player.set_hand(currplayer, Deck.deal(currdeck))
        Player.set_split_hand(currplayer, Deck.deal(currdeck))
        Player.set_split(currplayer, True)
        Player.set_hand_score(currplayer,\
            (Deck.card_value(Player.get_hand(currplayer, 0)) + \
                (Deck.card_value(Player.get_hand(currplayer, 1)))))
        Player.set_split_hand_score(currplayer,\
            (Deck.card_value(Player.get_split_hand(currplayer, 0)) + \
                (Deck.card_value(Player.get_split_hand(currplayer, 1)))))
        numcards1 = 2
        numcards2 = 2
        for i in range(numcards1):
            if ((Player.get_hand(currplayer, i).rank == 'A') and\
                (Player.get_ace_index(currplayer, i) != 1)):
                    Player.set_ace_index(currplayer, i)
        userinput = 'y'
        while self.check_user_input(userinput):
            print("Hand 1:")
            for i in range(numcards1):
                print("{}{}".format(Player.get_hand(currplayer, i).rank,\
                    Player.get_hand(currplayer, i).suit))
            Player.bust(currplayer)
            Player.set_num_cards(currplayer, numcards1 + 1)
            print("{}'s hand1 score: {}\n".format(Player.get_name(currplayer), \
                Player.get_hand_score(currplayer)))
            if Player.get_hand_score(currplayer) == 21:
                print("You got blackjack!")
                break
            if Player.bust(currplayer):
                print("You bust!")
                break
            userinput = input("Would you like to hit on hand 1? (Y/N)")
            print("\n")
            if self.check_user_input(userinput):
                Player.set_hand(currplayer, Deck.deal(currdeck))
                if Player.get_hand(currplayer, numcards1).rank == 'A':
                    Player.set_ace_index(currplayer, i)
                Player.set_hand_score(currplayer,\
                    ((Deck.card_value(Player.get_hand(currplayer, numcards1))) + \
                        (Player.get_hand_score(currplayer))))
                numcards1 += 1
                #Player.set_num_cards(currplayer, numcards1)
        userinput = 'y'
        Player.clear_ace_index(currplayer)
        for i in range(numcards2):
            if Player.get_split_hand(currplayer, i).rank == 'A':
                Player.set_ace_index(currplayer, i)
        while self.check_user_input(userinput):
            print("Hand 2:")
            for i in range(numcards2):
                print("{}{}".format(Player.get_split_hand(currplayer, i).rank,\
                    Player.get_split_hand(currplayer, i).suit))
            Player.split_bust(currplayer)
            Player.set_num_cards(currplayer, numcards2 + 1)
            print("{}'s hand2 score: {}\n".format(Player.get_name(currplayer), \
                Player.get_split_hand_score(currplayer)))
            if Player.get_split_hand_score(currplayer) == 21:
                print("You got blackjack!")
                break
            if Player.get_split_hand_score(currplayer) >= 22:
                print("You bust!")
                break
            userinput = input("Would you like to hit on hand 2? (Y/N)")
            print("\n")
            if self.check_user_input(userinput):
                Player.set_split_hand(currplayer, Deck.deal(currdeck))
                if Player.get_split_hand(currplayer, numcards2).rank == 'A':
                    Player.set_ace_index(currplayer, i)
                Player.set_split_hand_score(currplayer,\
                    (Deck.card_value(Player.get_split_hand(currplayer, numcards2)))\
                        + (Player.get_split_hand_score(currplayer)))
                numcards2 += 1
        Player.set_stand(currplayer, True)

    def insurance(self, currplayer):
        "Asks the players if they want to buy insurance"
        if currplayer.am_i_human():
            userinput = input("{}, Would you like to buy insurance?(Y/N) "\
                .format(Player.get_name(currplayer)))
            if self.check_user_input(userinput):
                Player.set_insurance(currplayer, True)
                sidebet = input("How much would you like to put on insurance? ")
                Player.set_side_bet(currplayer, sidebet)

    def to_file(self, pickle_file, players = []):
        """Write the list players to the file pickle_file."""
        with open(pickle_file, 'wb') as file_handle:
            pickle.dump(players, file_handle, pickle.HIGHEST_PROTOCOL)

    def from_file(self, pickle_file):
        """Read the contents of pickle_file, decode it, and return it as players."""
        with open(pickle_file, 'rb') as file_handle:
            players = pickle.load(file_handle)
        return players