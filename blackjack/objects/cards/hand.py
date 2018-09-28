from blackjack.objects.cards.deck import Card


class Hand(object):
    """
    Class to represent a hand of playing cards. The state of a hand has two states:
    hittable, or stood. It is represented by the attribute: stood.

    """

    def __init__(self, label=''):
        self.cards = []
        self.stood = False

    def split_cards(self):
        if len(self.cards) != 2:
            raise RuntimeError("You can not split when you don't have two cards.")
        new_hand_card = self.cards.pop()

        return new_hand_card

    def restart(self):
        """
        Function to reset a hand. Empties the list of hands.

        :return:
        """
        self.cards = []

    def add_card(self, card):
        """
        Function used to add a card into the user's hand.

        Will not add a card, if the state of the hand is in stood.

        :param card:
        :return:
        """
        if self.stood:
            raise RuntimeError("Can't add cards after you have stood!")
        if not isinstance(card, Card):
            raise TypeError("Need to add cards of type Card into the hand!")

        self.cards.append(card)

    def get_value(self):
        """
        Function to return the total value of the hand.

        :return: total_val (int)
        """
        total_val = 0
        for card in self.cards:
            if card.get_rank() >= 10:
                total_val += 10
            else:
                total_val += card.get_rank()
        return total_val

    def get_soft_value(self):
        """
        Function to return the soft value of the hand.

        :return: total_val (int)
        """
        total_val = 0  # total soft value to be returned
        numaces = 0  # keep track of the number of aces

        # add up the cards and keep track of the number of aces
        for card in self.cards:
            if card.get_rank() == 1:
                numaces += 1
            elif card.get_rank() >= 10:
                total_val += 10
            else:
                total_val += card.get_rank()

        # add up the aces
        for i in range(numaces):
            if total_val + 11 < 21:
                total_val += 11
            else:
                total_val += 1
        return total_val

    def get_cards(self, numerical=False):
        """
        Get a list of the cards, or get the numerical value of each of the cards
        1-10.

        :param numerical: (bool) a flag to return the list of cards (strs), or a list of their values.
        :return: (list) a list of the cards in this hand.
        """
        if numerical:
            cards = []
            for card in self.cards:
                if card.get_rank() >= 10:
                    cards.append(10)
                else:
                    cards.append(card.get_rank())
            return cards
        return self.cards

    def can_hit(self):
        """
        Helper function to determine if this hand is hittable.
        :return: (bool)
        """
        if self.get_value() < 21 and not self.stood:
            return True
        else:
            return False

    def stand(self):
        """
        Makes hand stand and freezes the hand from hitting.

        :return:
        """
        self.stood = True
