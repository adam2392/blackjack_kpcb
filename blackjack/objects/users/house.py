from blackjack.objects.users.base import BaseUser


class House(BaseUser):
    bankroll = None

    def __init__(self):
        self.bankroll = 1e9

    def __repr__(self):
        return "The House!"
