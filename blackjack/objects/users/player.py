
class Player(object):
    age = None
    amt_buyin = None
    amt_cashout = None
    bankroll = None

    def __init__(self, name, age, amt_buyin):
        self.name = name
        self.age = age
        self.amt_buyin = amt_buyin
        self.bankroll = amt_buyin

        if age < 18:
            raise ValueError("You can not play blackjack and gamble if you are less than 18 y/o!")

    def cash_out(self):
        self.amt_cashout = self.bankroll

    def win(self, amt):
        if not isinstance(amt, float) and not isinstance(amt, int):
            raise AttributeError("Won amount has to be in the form of a number!")

        self.bankroll += amt

    def lose(self, amt):
        if not isinstance(amt, float) and not isinstance(amt, int):
            raise AttributeError("Lost amount has to be in the form of a number!")

        self.bankroll -= amt