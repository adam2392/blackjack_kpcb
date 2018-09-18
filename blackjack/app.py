import argparse

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

    def add_player(self, name, buy_in, age):
        self.game.add_player(Player(name=name, age=age, amt_buyin=buy_in))

    def cash_out_player(self, name):
        self.game.remove_player(player_ind=name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='BLACKJACK', description='Blackjack game with '
                                                                   'optional help from a'
                                                                   'learning agent,'
                                                                   ' monte-carlo simulator,'
                                                                   ' or brute-force counter')
    parser.add_argument('cmd', choices=['start', 'add_player', 'cash_out', 'help', 'quit'])

    # initialize application
    app = App()

    # run terminal in infinite loop
    while True:
        astr = input('$: ')

        # parse the arguments
        try:
            args = parser.parse_args(astr.split())
        except SystemExit:
            # trap argparse error message
            print('error')
            continue

        # determine what engine of the game it should be
        if args.cmd in ['start']:
            print('doing', args.cmd)

            app.start_game()
        elif args.cmd in ['add_player']:
            print("Adding player to game! ")

            app.add_player()
        elif args.cmd in ['cash_out']:
            print("Cashing out player!")

            app.cash_out_player()
        elif args.cmd == 'help':
            parser.print_help()
        else:
            print('done')

            app.end_game()
            break
