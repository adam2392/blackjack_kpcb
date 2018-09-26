from blackjack.config import params
from blackjack.objects.game.deck import Deck
from blackjack.objects.game.game import Game
from blackjack.objects.game.hand import Hand
from blackjack.objects.users.house import House
from blackjack.objects.users.player import Player


class PlayBlackjack(Game):
    def __init__(self, numdecks, house):
        super(PlayBlackjack, self).__init__()
        self.numdecks = numdecks
        self.house = House()
        self.players = dict()

        self.in_play = False  # initialize to false, so deal can start

        # initialize deck to start playing
        self._init_mydeck()

    def add_player(self, player):
        if not isinstance(player, Player):
            raise TypeError("Passed in player has to be of type Player!")

        if player.player_identifier in self.players.keys():
            raise ValueError("Enter more information about your name, or add a number at the end!"
                             "There is already a player with your name, age and buy in amount..."
                             "Sorry about that.")
        self.players[player.player_identifier] = player

    def get_players(self):
        return self.players.values()

    def remove_player(self, player):
        if not isinstance(player, Player):
            raise ValueError("A Player object needs to be passed in!")

        if player.player_identifier not in self.players.keys():
            raise KeyError("Player is not a part of the game, so we can't remove this player!")

        self.players.pop(player.player_identifier)
        return 1

    def restart(self):
        self._init_mydeck()
        self.in_play = False
        self.house.restart()
        for player in self.get_players():
            player.restart()

    def _init_mydeck(self):
        # initialize mydeck and set it
        self.mydeck = Deck(self.numdecks)
        self.mydeck.shuffle()

    def deal(self):
        """
        Function to deal the initial hand to players
        :return:
        """
        for player in self.get_players():
            if player.get_total_bet() == 0:
                raise RuntimeError("Can't start until all players have bet! Either remove"
                                   "player, or place a bet. Player has {} bet".format(player.get_total_bet()))

        if self.in_play == False:
            # deal to each player
            for player_key in self.players:
                player = self.players[player_key]
                player.deal_hand(self._init_deal())

            # deal to house
            self.house.deal_hand(self._init_deal())

            self.in_play = True
        else:
            raise RuntimeError("You can't deal while game is still in play!"
                               "End game first!")

    def _init_deal(self):
        """
        Helper function to return an initial hand
        :return:
        """
        hand = Hand()
        # deal two cards
        for i in range(2):
            # deal to player
            card = self.mydeck.deal_card()
            hand.add_card(card)

        return hand

    def hit(self, playerhand):
        """
        Function to hit the player's hand.

        If bust, then in_play gets set to false and
        the game ends. The user is allowed then to rebet.

        If player loses, then the player loses bet.

        :return:
        """
        if self.in_play:
            card = self.mydeck.deal_card()
            playerhand.add_card(card)

    def stand(self, hand=None):
        """
        Function to stand on player's hand.

        If the player loses, then player loses bet.

        The dealer's hand is hit until it reaches 17.

        :return:
        """
        if hand is not None:
            hand.stand()
        else:
            # run a loop to play out the dealer's hand
            while self.in_play:
                # dealer's absolute value is still under 17
                if self.house.hand.get_value() < 17 and self.house.hand.get_soft_value() < 17:
                    card = self.mydeck.deal_card()
                    self.house.hand.add_card(card)
                # dealer has soft hand above 17
                elif self.house.hand.get_soft_value() > 17:
                    self.in_play = False
                # handle case of soft 17
                elif self.house.hand.get_soft_value() == 17 and self.house.hand.get_value() < 17:
                    # dealer hits soft 17
                    if params.DEALER_HITS_SEVENTEEN:
                        card = self.mydeck.deal_card()
                        self.house.hand.add_card(card)
                    # dealer does not hit soft 17
                    else:
                        self.in_play = False
                else:
                    self.in_play = False

    def determine_outcomes(self):
        # define a helper lambda function to get the end hand value
        end_hand_val = lambda x: max(x.get_value(), x.get_soft_value())

        if not self.in_play:
            # get the value of the house hand
            dealer_val = end_hand_val(self.house.hand)

            # determine loss/win outcome for each player
            for player in self.get_players():
                for ihand, hand in enumerate(player.get_hands()):
                    # determine loss or win
                    player_val = end_hand_val(hand)

                    if player_val > 21:
                        player.lose(ihand)

                    elif dealer_val > 21:
                        player.win(ihand)

                    # if loss
                    elif player_val > dealer_val:
                        # player wins
                        player.win(ihand)
                    else:
                        # player loses
                        player.lose(ihand)

    def split(self, _player):
        """
        Function to split cards!

        :return:
        """
        player = self.players[_player.player_identifier]

        # place bet
        player.place_bet(player.get_bet())

        # add a hand to player
        hands = []
        for card in player.hand.get_cards():
            hand = Hand()
            hand.add_card(card)
            hands.append(hand)
        player.deal_hand(hand)

        # for each hand hit
        for hand in player.get_hands():
            self.hit(hand)

    def double(self, _player):
        """
        Function to double your bet for only one more card
        :return:
        """
        player = self.players[_player.player_identifier]

        # place bet
        player.place_bet(player.get_bet())

        # hit once
        self.hit(player)

        # stand
        self.stand(player)

    def check_player_blackjack(self, hand):
        """
        Function to check if a player hand has a blackjack.

        :return: True/False (bool)
        """
        if hand.get_soft_value() == params.BLACKJACK:
            return True
        else:
            return False

    def check_dealer_blackjack(self):
        """
        Function to check if a dealer hand has a blackjack.

        :return: True/False (bool)
        """

        if self.house.hand.get_soft_value() == params.BLACKJACK:
            return True
        else:
            return False
