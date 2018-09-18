
class House(object):
    bankroll = None

    def __init__(self):
        self.bankroll = 1e9

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