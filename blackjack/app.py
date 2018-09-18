from blackjack.config import params
from blackjack.objects.game.blackjack import Blackjack
from blackjack.objects.users.house import House
from blackjack.objects.users.player import Player


class App(object):
    players = []
    game = None

    def __init__(self, num_players=1, names=['John Doe'], ages=[18], amt_buyins=[500]):
        self.house = House()

        if num_players > 6:
            raise ValueError("You can not have more then 6 players playing blackjack at a time!")

        # initialize players
        for i in range(num_players):
            name = names[i]
            age = ages[i]
            amt_buyin = amt_buyins[i]

            self.players.append(Player(name=name, age=age, amt_buyin=amt_buyin))

    def start_game(self):
        self.game = Blackjack(numdecks=params.NUMDECKS, players=self.players, house=self.house)
        self.game.start_game()

    def end_game(self):
        self.game.end_game()


if __name__ == '__main__':

