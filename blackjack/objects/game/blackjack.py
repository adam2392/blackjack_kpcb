from blackjack.objects.game.game import Game


class PlayBlackjack(Game):
    def __init__(self, numdecks, players, house):
        # super(Blackjack, self).__init__()
        self.numdecks = numdecks
        self.players = players
        self.house = house

    def _init_mydeck(self):
        # initialize mydeck and set it
        self.mydeck = []
        for i in range(self.numdecks):
            self.mydeck.append(Deck())

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_ind):
        self.players[player_ind] = []

    def deal(self):
        for player in self.players:
            # receive a card
            pass
