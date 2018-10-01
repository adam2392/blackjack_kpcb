from blackjack.objects.users.base import BaseUser
from blackjack.objects.cards.hand import Hand

"""
.. module:: users.house
   :synopsis: A module to store user related functionality for the House.

.. moduleauthor:: Adam Li <adam2392@gmail.com>

"""


class House(BaseUser):
    """
    The House class for the House user in a blackjack game.

    You would call this class in conjunction with :class:`Player` and :class:`BlackjackGame`.

    .. note::

       An example of initialization is this:
        house = House()

    """

    def __init__(self):
        # self.bankroll = 1e9
        self.hand = None

    def __repr__(self):
        return "The House!"

    def restart(self):
        """
        A helper function to reset the house's hand to None.

        :return: None
        """
        self.hand = None

    def deal_hand(self, hand):
        """
        Deals a hand to the house user.

        :param hand: a Hand object that will act as the house's hand.
        :return: None
        """
        if self.hand is not None:
            raise RuntimeError("Can't be dealt another hand, while in play!")
        if not isinstance(hand, Hand):
            raise TypeError("passed in hand to the house needs to be of type Hand!")

        self.hand = hand

    def lose(self):
        self.hand = None

    def win(self):
        self.hand = None

    @property
    def face_up_card(self):
        """
        A property of the house. They will always have a defined
        face up card, which is the first card they are dealt.

        :return: the first card they are dealt.
        """
        return self.hand.get_cards()[0]
