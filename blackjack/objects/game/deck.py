import random

from blackjack.config import params


def cmp(a, b):
    return (a > b) - (a < b)


class Card(object):
    """
    Class to represent a standard playing card.

    Attributes:
      suit: integer 0-3 (0=clubs, 1=diam, 2=heart, 3=spade)
      rank: integer 1-13 (10=j, 11=q, 12=k, 13=A
    """

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation."""
        return '%s of %s' % (Card.rank_names[self.get_rank()],
                             Card.suit_names[self.get_suit()])

    def __repr__(self):
        return '%s of %s' % (Card.rank_names[self.get_rank()],
                             Card.suit_names[self.get_suit()])

    def __cmp__(self, other):
        """Compares this card to other, first by suit, then rank.

        Returns a positive number if this > other; negative if other > this;
        and 0 if they are equivalent.
        """
        t1 = self.get_suit(), self.get_rank()
        t2 = other.get_suit(), other.get_rank()
        return cmp(t1, t2)

    def __lt__(self, other):
        t1 = self.get_suit(), self.get_rank()
        t2 = other.get_suit(), other.get_rank()
        return cmp(t1, t2)

    def __eq__(self, other):
        t1 = self.get_suit(), self.get_rank()
        t2 = other.get_suit(), other.get_rank()
        if t1[0] == t2[0] and t1[1] == t2[1]:
            return True
        else:
            return False

    def get_rank(self):
        return self.rank

    def get_suit(self):
        return self.suit


class Deck(object):
    """
    Class for representing a deck of cards.

    Essentially creates a stack of cards as a data structure to hold the deck.

    Attributes:
      cards: list of Card objects.

    """
    numcards = params.NUMCARDS_IN_DECK

    def __init__(self, numdecks=1):
        self.cards = []
        self.numdecks = numdecks
        for i in range(numdecks):
            for suit in range(4):
                for rank in range(1, 14):
                    card = Card(suit, rank)
                    self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def __repr__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()
