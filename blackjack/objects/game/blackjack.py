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
        # self.players = players
        self.house = House()
        self.players = dict()

        # state variables of the game
        self.hDealer = Hand()
        self.hPlayer = Hand()
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

    def remove_player(self, player):
        self.players.pop(player.player_identifier)
        return 1

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
            # deal to each player
            for iplayer in self.players:
                player = self.players[iplayer.player_identifier]
                player.deal_hand(self._init_deal())

            # deal to house
            self.house.deal_hand(self._init_deal())
        else:
            raise RuntimeError("You can't deal while game is still in play!"
                               "End game first!")

    def _init_deal(self):
        """
        Helper function to return an initial hand
        :return:
        """
        # deal two cards
        for i in range(2):
            # deal to player
            card = self.mydeck.deal_card()
            hand = Hand()
            hand.add_card(card)

        return hand

    def hit(self, player):
        """
        Function to hit the player's hand.

        If bust, then in_play gets set to false and
        the game ends. The user is allowed then to rebet.

        If player loses, then the player loses bet.

        :return:
        """
        pass

    def stand(self, player):
        """
        Function to stand on player's hand.

        If the player loses, then player loses bet.

        The dealer's hand is hit until it reaches 17.

        :return:
        """
        # run a loop to play out the dealer's hand
        while self.in_play:
            # dealer's absolute value is still under 17
            if self.hDealer.get_value() < 17 and self.hDealer.get_soft_value() < 17:
                card = self.mydeck.deal_card()
                self.hDealer.add_card(card)
            # dealer has soft hand above 17
            elif self.hDealer.get_soft_value() > 17:
                self.in_play = False
            # handle case of soft 17
            elif self.hPlayer.get_soft_value() == 17:
                # dealer hits soft 17
                if params.DEALER_HITS_SEVENTEEN:
                    card = self.mydeck.deal_card()
                    self.hDealer.add_card(card)
                # dealer does not hit soft 17
                else:
                    self.in_play = False
            else:
                self.in_play = False

        # determine loss or win
        end_hand_val = lambda x: max(x.get_value(), x.get_soft_value())
        player_val = end_hand_val(self.hPlayer)
        dealer_val = end_hand_val(self.hDealer)

        # if loss
        if player_val > dealer_val:
            # player wins

            print("player wins!")
        else:
            # player loses
            print("player loses!")

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

    def check_player_blackjack(self, _player):
        """
        Function to check if a player hand has a blackjack.

        :return: True/False (bool)
        """
        player = self.players[_player.player_identifier]
        if player.hand.get_soft_value() == params.BLACKJACK:
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
