from blackjack.objects.users.base import BaseUser


class Player(BaseUser):
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
