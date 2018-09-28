from blackjack.objects.users.base import BaseUser
from blackjack.objects.cards.hand import Hand

class Player(BaseUser):
    """
    A class/object that is a player. This is user of the cards.

    This object handles all cards state information for a player, such as their hands, and winning, or losing
    each hand.

    :member name: (str) the unique name of a player.
    """
    def __init__(self, name):
        self.name = name
        self.hands = []

        # self.age = float(age)
        # self.amt_buyin = float(amt_buyin)
        # self.bankroll = float(amt_buyin)
        # self.amt_bet = []
        # self.total_bet = 0
        # if self.age < 18:
        #     raise ValueError("You can not play blackjack and gamble if you are less than 18 y/o!")

    def __str__(self):
        return "player: {}".format(self.name)

    def __repr__(self):
        return "player: {}".format(self.name)

    def __cmp__(self, player):
        return "player: {}".format(self.name) == "player: {}".format(player.name)

    @property
    def player_identifier(self):
        return "player: {}".format(self.name)

    def deal_hand(self, hand):
        """
        Deals an extra hand to the player. This is called when a player splits.

        It can also be called in future versions, when a player decides to add more then 1 hand.

        :param hand: (Hand) a hand object that will be appended to the player's hands.
        :return:
        """
        if not isinstance(hand, Hand):
            raise TypeError("passed in hand, has to be of type Hand!")

        if len(self.hands) == 4:
            raise RuntimeError("A player can not split hands more then 4 times. "
                               "Choose to hit, stand, or double!")
        self.hands.append(hand)

    def restart(self):
        """
        A function to restart a player's cards mode.

        It empties out all hands for a player.
        :return:
        """
        self._reset()

    def get_hands(self):
        """
        Access function to return the hands a player has

        :return: (list) a list of the hand objects belonging to a player
        """
        return self.hands

    def lose(self, ihand):
        """
        Function to handle when a player loses a hand

        :param ihand: (int) the index of the hand the player is on (0-3)
        :return:
        """
        # self.amt_bet[ihand] = 0
        self.hands[ihand] = 0

        # reset state after handling all the hands
        if ihand == len(self.hands):
            self._reset()

    def win(self, ihand):
        """
        Function to handle when a player wins a hand.

        :param ihand: (int) the index of the hand the player is on (0-3)
        :return:
        """
        # self.bankroll += self.amt_bet[ihand]
        # self.amt_bet[ihand] = 0
        self.hands[ihand] = 0

        # reset state after we've handled all our hands
        if ihand == len(self.hands):
            self._reset()

    def cash_out(self):
        """
        Function for player to cash out.

        To be implemented in a future version
        :return:
        """
        # self.amt_cashout = self.bankroll
        pass

    def place_bet(self, bet):
        """
        Function for player to place a bet.

        To be implemented in a future version
        :param bet:
        :return:
        """
        # self.bankroll -= bet
        # self.total_bet += bet
        # self.amt_bet.append(bet)
        pass

    def get_total_bet(self):
        """
        Function to get the total bet of a player during a play state.

        To be implemented in a future version
        :return:
        """
        pass
        # return self.total_bet

    def _reset(self):
        self.hands = []
        self.amt_bet = []
        self.total_bet = 0
