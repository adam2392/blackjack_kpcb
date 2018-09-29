from blackjack.config import params
from blackjack.objects.cards.deck import Deck
from blackjack.objects.game.game import Game
from blackjack.objects.cards.hand import Hand
from blackjack.objects.users.house import House
from blackjack.objects.users.player import Player


class PlayBlackjack(Game):
    """
    The blackjack cards class/object. It is a wrapper for synchronizing all the interactions
    between cards objects and user objects.

    All players are stored in a dictionary, accessed by their name.

    The house is stored as a direct object, since there is only one house user.

    The game state is stored as an attribute: in_play.

    Attributes:
        numdecks: (int) the number of decks to use in this game

    """

    def __init__(self, numdecks):
        super(PlayBlackjack, self).__init__()

        # initialize the number of decks
        self.numdecks = numdecks

        # initialize the house object in this game
        self.house = House()

        # store all players in a dictionary
        self.players = dict()

        # initialize to false, so deal can start
        self.in_play = False

        # initialize deck to start playing
        self._init_mydeck()

    def add_player(self, player):
        """
        Function to add player to the game. It adds the player by their name to the dictionary of players.

        :param player: (Player) is a player to be added with a unique name identifier.
        :return:
        """
        if not isinstance(player, Player):
            raise TypeError("Passed in player has to be of type Player!")

        if player.player_identifier in self.players.keys():
            raise ValueError("Enter more information about your name, or add a number at the end!"
                             "There is already a player with your name, age and buy in amount..."
                             "Sorry about that.")
        self.players[player.player_identifier] = player

    def get_players(self):
        """
        Function to return all the player objects for this game.

        :return: (list) of Player objects
        """
        return self.players.values()

    def remove_player(self, player):
        """
        Removes a player from the game.

        :param player: (Player) the player to be removed from the game
        :return: 1 if successful
        """
        if not isinstance(player, Player):
            raise ValueError("A Player object needs to be passed in!")

        if player.player_identifier not in self.players.keys():
            raise KeyError("Player is not a part of the cards, so we can't remove this player!")

        self.players.pop(player.player_identifier)
        return 1

    def restart(self):
        """
        Function to restart the game by initializing it to a beginning game state of not in play, shuffle the
        decks of cards and reset player's hands.

        :return:
        """
        # reset deck and shuffle it
        self._init_mydeck()
        self.in_play = False

        # reset the house
        self.house.restart()

        # reset all players
        for player in self.get_players():
            player.restart()

    def freeze_play(self):
        self.in_play = False

    def _init_mydeck(self):
        # initialize mydeck and set it
        self.mydeck = Deck(self.numdecks)
        self.mydeck.shuffle()

    def deal(self):
        """
        Function to deal the initial hand to players. This is the function to begin game play state.

        You can not deal if the game has already started.

        :return:
        """
        # for player in self.get_players():
        #     if player.get_total_bet() == 0:
        #         raise RuntimeError("Can't start until all players have bet! Either remove"
        #                            "player, or place a bet. Player has {} bet".format(player.get_total_bet()))

        # if the game is not in play yet, start it
        if self.in_play == False:
            # deal to each player
            for player_key in self.players:
                player = self.players[player_key]
                player.deal_hand(self._init_deal())

            # deal to house
            self.house.deal_hand(self._init_deal())

            # set the game state to "in play"
            self.in_play = True
        else:
            raise RuntimeError("You can't deal while cards is still in play!"
                               "End cards first!")

    def _init_deal(self):
        """
        Helper function to return an initial hand. Meant to be called by the deal function to initialize the deal
        to each user (player and house).

        :return: (Hand) the hand object with two starting cards.
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
        the cards ends. The user is allowed then to rebet.

        If player loses, then the player loses bet.

        :return:
        """
        if self.in_play:
            card = self.mydeck.deal_card()
            playerhand.add_card(card)

    def is_in_play(self):
        return self.in_play

    def stand(self, hand=None):
        """
        Function to stand on player's hand.

        If the player loses, then player loses bet.

        The dealer's hand is hit until it reaches 17.

        :return:
        """
        # stands the hand
        if hand is not None and not hand.stood:
            hand.stand()

            players = self.get_players()
            all_stood = True
            for player in players:
                if any([not h.stood for h in player.get_hands()]):
                    all_stood = False
            # all hands are stood
            if all_stood:
                self.in_play = False
        else:
            # run a loop to play out the dealer's hand
            while self.house.hand.can_hit(ishouse=True):
                card = self.mydeck.deal_card()
                self.house.hand.add_card(card)

    def determine_outcomes(self):
        """
        Function to determine the outcomes of the game.
        
        :return:
        """
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

                        print("{} lost hand with {}!".format(player, hand.get_total_value()))
                    elif dealer_val > 21:
                        player.win(ihand)
                        print("{} won hand with {}!".format(player, hand.get_total_value()))

                    # if loss
                    elif player_val > dealer_val:
                        # player wins
                        player.win(ihand)
                        print("{} won hand with {}!".format(player, hand.get_total_value()))

                    else:
                        # player loses
                        player.lose(ihand)
                        print("{} lost hand with {}!".format(player, hand.get_total_value()))

    def split(self, player, hand):
        """
        Function to split a hand and add a hand to that player.

        :param player:
        :param hand:
        :return:
        """
        # player = self.players[_player.player_identifier]
        # place bet
        # player.place_bet(player.get_bet())

        # create a new hand from the current hand
        newhand = Hand()
        new_card_hand = hand.split_cards()
        newhand.add_card(new_card_hand)

        # add that hand to player
        player.deal_hand(newhand)

        # for each hand hit it once
        self.hit(hand)
        self.hit(newhand)

    def double(self, player, hand):
        """
        Function to double your bet for only one more card.

        :return:
        """
        # player = self.players[_player.player_identifier]
        # place bet
        # player.place_bet(player.get_bet())

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
        print(self.house.hand.get_soft_value())
        print(params.BLACKJACK)
        if self.house.hand.get_soft_value() == params.BLACKJACK:
            return True
        else:
            return False
