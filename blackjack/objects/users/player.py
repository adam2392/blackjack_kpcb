from blackjack.objects.users.base import BaseUser


class Player(BaseUser):
    age = None
    amt_buyin = None
    amt_cashout = None
    bankroll = None

    def __init__(self, name, age, amt_buyin):
        self.name = name
        self.age = float(age)
        self.amt_buyin = amt_buyin
        self.bankroll = amt_buyin
        self.amt_bet = 0
        self.hands = []

        if self.age < 18:
            raise ValueError("You can not play blackjack and gamble if you are less than 18 y/o!")

    def __str__(self):
        return "player: {} ({})".format(self.name, self.age)

    def __repr__(self):
        return "player: {} ({})".format(self.name, self.age)

    @property
    def player_identifier(self):
        return "player: {} ({}) ({})".format(self.name, self.age, self.amt_buyin)

    def deal_hand(self, hand):
        if len(self.hands) == 4:
            raise RuntimeError("A player can not split hands more then 4 times. "
                               "Choose to hit, stand, or double!")
        self.hands.append(hand)

    def get_hands(self):
        return self.hands

    def cash_out(self):
        self.amt_cashout = self.bankroll

    def lose(self):
        self.amt_bet = 0

    def win(self):
        self.bankroll += self.amt_bet
        self.amt_bet = 0

    def place_bet(self, bet):
        self.bankroll -= bet
        self.amt_bet += bet

    def get_bet(self):
        return self.amt_bet
