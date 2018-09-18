from blackjack.objects.game.deck import Hand


class BaseUser(object):
    amt = 0

    def assign_hand(self, hand):
        if not isinstance(hand, Hand):
            raise AttributeError("Need to assign a type of Hand to the player!")
        self.hand = hand

    def win(self, amt):
        if not isinstance(amt, float) and not isinstance(amt, int):
            raise AttributeError("Won amount has to be in the form of a number!")

        self.bankroll += amt

    def lose(self, amt):
        if not isinstance(amt, float) and not isinstance(amt, int):
            raise AttributeError("Lost amount has to be in the form of a number!")

        self.bankroll -= amt
