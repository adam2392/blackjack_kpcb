import argparse

from blackjack.config import params
from blackjack.objects.game.blackjack import PlayBlackjack
from blackjack.objects.users.house import House
from blackjack.objects.users.player import Player


class App(object):
    players = []
    game = None

    def __init__(self):
        # initialize cards with a house player
        self.house = House()

        # start with 0 players
        self.num_players = 0

        # initialize an empty game
        self.game = PlayBlackjack(numdecks=params.NUMDECKS)

    def start_game(self):
        """
        Function to start the game. Calls game's starting function (e.g. deal, start, etc.)

        Requires that there are active players.
        :return:
        """
        # check if there are players
        if len(self.game.get_players()) == 0:
            print("Please add players before trying to start the game!")
            return 0

        # deals to the players
        self.game.deal()

        # loop through players, hands
        for player in self.game.get_players():
            print("Hello {} player".format(player))

            for hand in player.get_hands():

                # start game state -> hit, stand, split, double, surrender -> house outcome
                while self.game.is_in_play():
                    print("What action would you like to take? (hit, stand, double, split)")

                    # display player hand
                    print("You have {} with total value of {}, or {}".format(
                        hand, hand.get_value(), hand.get_soft_value()))

                    # query action
                    action = get_game_info()

                    if action == 'hit':
                        self.game.hit(hand)
                    elif action == 'stand':
                        self.game.stand(hand)
                        break
                    elif action == 'double':
                        self.game.double(player, hand)
                    elif action == 'split':
                        self.game.split(player, hand)
                    else:
                        print("Enter a valid action to take!")

        # now dealer gets dealt cards
        self.game.stand()

        # determine outcomes
        self.game.determine_outcomes()

        return 1

    def restart_game(self):
        """
        Function to restart the game, calls the game.restart() command

        :return:
        """
        # restarts the game
        self.game.restart()

    def end_game(self):
        print("Ending game now! Thanks for playing.")
        self.game.end_game()

    def add_player(self, name):
        if self.num_players > 6:
            raise ValueError("You can not have more then 6 players playing blackjack at a time!")

        self.game.add_player(Player(name=name))
        self.num_players += 1

    def cash_out_player(self, name):
        if self.num_players == 0:
            raise ValueError("You can not remove a player if there are none!")

        self.game.remove_player(name)
        self.num_players -= 1


class SubApp():

    @staticmethod
    def check_blackjack(game):
        """
        Function wrapper to check blackjacks

        To be implemented in future version: having multiple starting hands for players.
        :return: (tuple) of the house_bj outcome and the player_bjs outcome (as a list)
        """
        # initialize list to store outcome of player blackjacks
        player_bjs = []
        for player in game.get_players():
            # player_bj = []
            for hand in player.get_hands():
                is_bj = game.check_player_blackjack(hand)
                player_bjs.append(is_bj)

        # check for bj
        house_bj = game.check_dealer_blackjack()
        return house_bj, player_bjs

    @staticmethod
    def check_outcome(self, game):
        game.check_outcome()


def get_player_info():
    parser = argparse.ArgumentParser(usage="Please enter the player's name. "
                                           "(e.g. Adam Li) "
                                           "If the name is not unique in our system, please enter numbers afterwards. "
                                           "(e.g. Adam Li001)")
    parser.add_argument('name', type=str)

    while True:
        print("Enter a valid players name please who wants to start playing!")
        astr = input('$: ')

        try:
            args = parser.parse_args(astr.split())
        except SystemExit:
            # trap argparse error message
            print('error please enter a valid name')
            continue

        name = args.name
        if len(name) > 0:
            break

    print("Adding player {}".format(name))
    return name


def get_cashout_info():
    parser = argparse.ArgumentParser(usage="Please enter the player's name who will"
                                           "be cashing out and leaving!")
    parser.add_argument('name', type=str)

    while True:
        print("Enter a valid players name please to cash out!")
        astr = input('$: ')

        try:
            args = parser.parse_args(astr.split())
        except SystemExit:
            # trap argparse error message
            print('error please enter a valid name')
            continue

        name = args.name
        if len(name) > 0:
            break

    print("Cashing out player {}".format(name))
    return name


def get_game_info():
    parser = argparse.ArgumentParser(prog='BLACKJACK',
                                     usage="You are on your hand. \n"
                                           "Please enter one of the following commands to proceed: \n"
                                           "hit, double, split, stand, help, or quit")
    parser.add_argument('cmd', choices=['hit', 'double',
                                        'split', 'stand',
                                        'help', 'quit'])
    parser.print_help()
    while True:
        print("Enter a valid command!")
        astr = input('$: ')

        try:
            args = parser.parse_args(astr.split())
        except SystemExit:
            # trap argparse error message
            print('error please enter a valid command')
            continue

        action = args.cmd
        break

    return action


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='BLACKJACK', description='Blackjack cards with '
                                                                   'optional help from a'
                                                                   'learning agent,'
                                                                   ' monte-carlo simulator,'
                                                                   ' or brute-force counter',
                                     usage="This is the blackjack cards app made by Adam Li. \n"
                                           "Please enter one of the following commands to begin: \n"
                                           "start, add_player, help, or quit")
    parser.add_argument('cmd', choices=['start',
                                        'add_player',
                                        'cash_out',
                                        'help', 'quit'])

    # initialize application
    app = App()

    # print help at the beginning
    parser.print_help()

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

        # determine what engine of the cards it should be
        if args.cmd in ['start']:
            # start cards
            start_status = app.start_game()

        elif args.cmd in ['add_player']:
            player_name = get_player_info()
            app.add_player(player_name)

        elif args.cmd in ['cash_out']:
            player_name = get_cashout_info()
            app.cash_out_player(player_name)

        elif args.cmd == 'help':
            parser.print_help()

        elif args.cmd == 'quit':
            app.end_game()
            break
