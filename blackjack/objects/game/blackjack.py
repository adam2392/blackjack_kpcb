from blackjack.config import params

from blackjack.objects.game.game import Game
from blackjack.objects.game.deck import Deck
from blackjack.objects.game.hand import Hand


class PlayBlackjack(Game):
    def __init__(self, numdecks, players, house):
        super(PlayBlackjack, self).__init__()
        self.numdecks = numdecks
        self.players = players
        self.house = house

        # state variables of the game
        self.hDealer = Hand()
        self.hPlayer = Hand()
        self.in_play = False  # initialize to false, so deal can start

        # initialize deck to start playing
        self._init_mydeck()

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_ind):
        self.players[player_ind] = []

    def restart(self):
        self._init_mydeck()

    def _init_mydeck(self):
        # initialize mydeck and set it
        self.mydeck = Deck(self.numdecks)
        self.mydeck.shuffle()

    def deal(self):
        """
        Function to deal the initial hand to players
        :return:
        """
        if self.in_play == False:
            for i in range(2):
                # deal to player
                card = self.mydeck.deal_card()
                self.hPlayer.add_card(card)

                # then deal to house
                card = self.mydeck.deal_card()
                self.hDealer.add_card(card)
        else:
            raise RuntimeError("You can't deal while game is still in play!"
                               "End game first!")

    def hit(self):
        """
        Function to hit the player's hand.

        If bust, then in_play gets set to false and
        the game ends. The user is allowed then to rebet.

        If player loses, then the player loses bet.

        :return:
        """
        pass

    def stand(self):
        """
        Function to stand on player's hand.

        If the player loses, then player loses bet.

        The dealer's hand is hit until it reaches 17.

        :return:
        """
        pass

    def check_player_blackjack(self):
        """
        Function to check if a player hand has a blackjack.

        :return: True/False (bool)
        """

        if self.hPlayer.get_soft_value() == params.BLACKJACK:
            return True
        else:
            return False

    def check_dealer_blackjack(self):
        """
        Function to check if a dealer hand has a blackjack.

        :return: True/False (bool)
        """

        if self.hDealer.get_soft_value() == params.BLACKJACK:
            return True
        else:
            return False
