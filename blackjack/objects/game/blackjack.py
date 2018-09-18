from blackjack.objects.game.game import Game


class Blackjack(Game):
    def __init__(self, numdecks, players, house):
        # super(Blackjack, self).__init__()
        self.numdecks = numdecks
        self.players = players
        self.house = house

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player_ind):
        self.players[player_ind] = []

    def deal(self):
        for player in self.players:
            # receive a card
            pass
