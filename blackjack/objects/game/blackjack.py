from blackjack.objects.game.game import Game

class Blackjack(Game):
    players = {}

    def __init__(self, numdecks=1):
        super(Blackjack, self).__init__()
        self.numdecks = numdecks

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players[player_ind] = []

    def deal(self):
        for player in self.players:
            # receive a card
            pass



