# Brandon Rupp
# CPSC 386-01
# 2022-03-15
# brandonrupp@csu.fullerton.edu
# @brupp34
#
# Lab 03-00
#
# This is the cards file that conatins the logic for the players
# for a Blackjack program.


"""This file has the player logic"""


class Player:
    """Player class for the BlackJack game"""

    def __init__(self, name, banknroll=10000):
        "Init a player with various variables"
        self._name = name
        self._balance = banknroll
        self._bet = int
        self._side_bet = int
        self._hand = []
        self._split_hand = []
        self._hand_score = int
        self._split_hand_score = int
        self._stand = False
        self._split = False
        self._insurance = False
        self._numcards = int
        self._black_jack = False
        self._ace_index = []
        for i in range(20):
            self._ace_index.append(0)

    def get_split(self):
        "Getter for split"
        return self._split

    def set_split(self, value):
        "Setter for split"
        self._split = value

    def get_name(self):
        "Getter for name"
        return self._name

    def get_balance(self):
        "Getter for balance"
        return int(self._balance)

    def set_balance(self, value):
        "Setter for balance"
        self._balance = value

    def get_bet(self):
        "Getter for bet"
        return int(self._bet)

    def get_black_jack(self):
        "Getter for blackjack"
        return self._black_jack

    def set_black_jack(self, value):
        "Setter for blackjack"
        self._black_jack = value

    def set_hand(self, value):
        "Setter for hand"
        self._hand.append(value)

    def set_bet(self, value=int):
        "Setter for bet"
        self._bet = value

    def get_hand(self, card_position=int):
        "Getter for hand"
        return self._hand[card_position]

    def set_split_hand(self, value=list):
        "Setter for split hand"
        self._split_hand.append(value)

    def get_split_hand(self, card_position=int):
        "Getter for split hand"
        return self._split_hand[card_position]

    def pop_player_card(self):
        "Returns popped player card"
        return self._hand.pop()

    def get_side_bet(self):
        "Getter for sidebet"
        return self._side_bet

    def set_side_bet(self, value):
        "Setter for sidebet"
        self._side_bet = value

    def get_hand_score(self):
        "Getter for handscore"
        return self._hand_score

    def get_insurance(self):
        "Getter for insurance"
        return self._insurance

    def set_insurance(self, value):
        "Setter for insurance"
        self._insurance = value

    def set_hand_score(self, value):
        "Setter for handscore"
        self._hand_score = value

    def set_split_hand_score(self, value=int):
        "Setter for split hand score"
        self._split_hand_score = value

    def get_split_hand_score(self):
        "Getter for split hand score"
        return self._split_hand_score

    def get_stand(self):
        "Getter for split stand"
        return self._stand
    
    def set_ace_index(self, value):
        "Sets the ace index"
        self._ace_index.insert(value, 1)

    def clear_ace_index(self):
        del(self._ace_index[:])
        for i in range(20):
            self._ace_index.append(0)
    
    def get_ace_index(self, value):
        return self._ace_index[value]

    def bust(self):
        "Checks bust with the Ace scores"
        if self._hand_score >= 22:
            for i in range(self._numcards + 1):
                if self._ace_index[i] == 1:
                    self._hand_score = (self._hand_score - 10)
                    del(self._ace_index[i])
                    self._ace_index.insert(i, 0)
                    return False
            return True
        return False

    def split_bust(self):
        "Checks bust with the Ace scores"
        if self._split_hand_score >= 22:
            for i in range(self._numcards + 1):
                if self._ace_index[i] == 1:
                    self._split_hand_score = (self._split_hand_score - 10)
                    del(self._ace_index[i])
                    self._ace_index.insert(i, 0)
                    return False
            return True
        return False
    
    def set_stand(self, value):
        "Setter for stand"
        self._stand = value

    def set_num_cards(self, value):
        "Setter for numcards"
        self._numcards = value

    def get_num_cards(self):
        "Getter for numcards"
        return int(self._numcards)

    def win_bet(self):
        "Adds player bet to their bank if they win the hand"
        self._balance = int(self._balance) + int(self._bet)

    def lose_bet(self):
        "Subracts player bet from their bank if they lose the hand"
        self._balance = int(self._balance) - int(self._bet)

    def win_side_bet(self):
        "Adds player side bet to their bank if dealer had blackjack"
        self._balance = int(self._balance) + int(self._side_bet)

    def lose_side_bet(self):
        "Subtract player side bet if dealer did not have blackjack"
        self._balance = int(self._balance) - int(self._side_bet)

    def round_reset(self):
        "No change to balance, reset the round"
        self._bet = 0
        self._side_bet = 0
        self._hand = []
        self._hand_score = 0
        self._stand = False
        self._numcards = 0
        self._split_hand = []
        self._split = False
        self._insurance = False
        self._black_jack = False
        self._split_hand_score = 0
        self.clear_ace_index()

    def am_i_human(self):
        "Checks to see if player is computer"
        return True


class Dealer(Player):
    "A subclass of player that contains the logic for the dealer"
    def __init__(self, name):
        "Initializes the dealer"
        self._name = name
        self._hand = []
        self._hand_score = int
        self._stand = False
        self._numcards = int
        self._ace_index = []
        for i in range(20):
            self._ace_index.append(0)

    def does_hit(self, value):
        "Checks to see if the dealer is going to hit"
        if (value <= 16) and (self._stand is False):
            return True
        return False

    def get_name(self):
        "Getter for name"
        return self._name

    def get_hand(self, card_position=int):
        "Getter for hand"
        return self._hand[card_position]

    def get_hand_score(self):
        "Getter for hand score"
        return self._hand_score

    def get_stand(self):
        "Getter for stand"
        return self._stand

    def get_numcards(self):
        "Getter for numcards"
        return self._numcards

    def set_hand(self, value):
        "Setter for hand"
        self._hand = value

    def set_hand_score(self, value):
        "Setter for hand score"
        self._hand_score = value

    def set_stand(self, value):
        "Setter for stand"
        self._stand = value

    def set_numcards(self, value):
        "Setter for numcards"
        self._numcards = value

    def am_i_human(self):
        "Checks to see if player is computer"
        return False

    def set_ace_index(self, value):
        "Sets the ace index"
        self._ace_index.insert(value, 1)

    def bust(self):
        "Checks bust with the Ace scores"
        if self.get_hand_score() >= 22:
            for i in range(self._numcards):
                if self._ace_index[i] == 1:
                    self._hand_score = (self._hand_score - 10)
                    del(self._ace_index[i])
                    self._ace_index.insert(i, 0)
                    return False
            return True
        return False