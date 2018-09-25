from blackjack.objects.game.deck import Deck, Card


class Hand(Deck):
    """
    Class to represent a hand of playing cards. It inherits
    functionality from a deck.

    """

    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def add_card(self, card):
        """
        Function used to add a card into the user's hand.

        :param card:
        :return:
        """
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
        total_val = 0
        numaces = 0
        for card in self.cards:
            if card.get_rank() == 1:
                numaces += 1
            elif card.get_rank() >= 10:
                total_val += 10
            else:
                total_val += card.get_rank()
        for i in range(numaces):
            if total_val + 11 < 21:
                total_val += 21
            else:
                total_val += 1
        return total_val

    def get_cards(self):
        return self.cards