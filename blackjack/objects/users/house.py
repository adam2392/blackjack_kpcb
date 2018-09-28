from blackjack.objects.users.base import BaseUser
from blackjack.objects.cards.hand import Hand


class House(BaseUser):
    def __init__(self):
        # self.bankroll = 1e9
        self.hand = None

    def __repr__(self):
        return "The House!"

    def restart(self):
        self.hand = None

    def deal_hand(self, hand):
        if self.hand is not None:
            raise RuntimeError("Can't be dealt another hand, while in play!")
        if not isinstance(hand, Hand):
            raise TypeError("passed in hand to the house needs to be of type Hand!")

        self.hand = hand

    def lose(self):
        self.hand = None

    def win(self):
        self.hand = None
