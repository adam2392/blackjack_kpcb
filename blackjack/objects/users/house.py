from blackjack.objects.users.base import BaseUser


class House(BaseUser):
    bankroll = None

    def __init__(self):
        self.bankroll = 1e9
        self.hand = None

    def __repr__(self):
        return "The House!"

    def restart(self):
        self.hand = None

    def deal_hand(self, hand):
        if self.hand is not None:
            raise RuntimeError("Can't be dealt another hand, while in play!")
        self.hand = hand

    def lose(self):
        self.hand = None

    def win(self):
        self.hand = None