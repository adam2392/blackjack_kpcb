from blackjack.objects.users.base import BaseUser


class Player(BaseUser):

    def __init__(self, name, age, amt_buyin):
        self.name = name
        self.age = float(age)
        self.amt_buyin = float(amt_buyin)
        self.bankroll = float(amt_buyin)
        self.amt_bet = []
        self.total_bet = 0
        self.hands = []

        if self.age < 18:
            raise ValueError("You can not play blackjack and gamble if you are less than 18 y/o!")

    def __str__(self):
        return "player: {} ({})".format(self.name, self.age)

    def __repr__(self):
        return "player: {} ({})".format(self.name, self.age)

    def __cmp__(self, player):
        return "player: {} ({})".format(self.name, self.age) == "player: {} ({})".format(player.name, player.age)

    @property
    def player_identifier(self):
        return "player: {} ({}) ({})".format(self.name, self.age, self.amt_buyin)

    def deal_hand(self, hand):
        if len(self.hands) == 4:
            raise RuntimeError("A player can not split hands more then 4 times. "
                               "Choose to hit, stand, or double!")
        self.hands.append(hand)

    def restart(self):
        self._reset()

    def get_hands(self):
        return self.hands

    def cash_out(self):
        self.amt_cashout = self.bankroll

    def lose(self, ihand):
        print(self.hands)
        print(self.amt_bet)
        self.amt_bet[ihand] = 0
        self.hands[ihand] = 0

        # reset state after handling all the hands
        if ihand == len(self.hands):
            self._reset()

    def win(self, ihand):
        self.bankroll += self.amt_bet[ihand]
        self.amt_bet[ihand] = 0
        self.hands[ihand] = 0

        # reset state after we've handled all our hands
        if ihand == len(self.hands):
            self._reset()

    def place_bet(self, bet):
        self.bankroll -= bet
        self.total_bet += bet
        self.amt_bet.append(bet)

    def get_total_bet(self):
        return self.total_bet

    def _reset(self):
        self.hands = []
        self.amt_bet = []
        self.total_bet = 0
