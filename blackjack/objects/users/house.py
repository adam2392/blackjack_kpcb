from blackjack.objects.users.base import BaseUser


class House(BaseUser):
    bankroll = None

    def __init__(self):
        self.bankroll = 1e9
