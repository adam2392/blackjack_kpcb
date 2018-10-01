import argparse

from blackjack.config import params
from blackjack.objects.game.blackjack import PlayBlackjack
from blackjack.objects.users.player import Player

from blackjack.teacher.base import BasicStrategyTeacher

from blackjack.utility.utils import get_game_info, get_cashout_info, get_player_info


class App(object):
    def __init__(self, TEACHERMODE=False):
        # start with 0 players
        self.num_players = 0

        # initialize an empty game
        self.game = PlayBlackjack(numdecks=params.NUMDECKS)

        self.TEACHERMODE = TEACHERMODE
        self.basic_strat = BasicStrategyTeacher()

        # create a stack of completed hands
        self.completed_hands = []
        self.in_play_hands = []

    def play_out_hand(self, player, hand):
        while hand.can_hit():
            # get the house hand's numerical values
            hhand = self.game.house.hand.get_cards(numerical=True)

            # does the player have a blackjack?
            playerbj = self.game.check_player_blackjack(hand)

            print("On player: {}".format(player.player_identifier))
            if playerbj:
                # pay out player 3 to 2
                print("you have a blackjack! Paid 3 to 2.")
                self.completed_hands.append(hand)
                break

            print("\nWhat action would you like to take? (hit, stand, double, split)")
            # display player hand
            print("\n", hand)

            # display suggested action
            if self.TEACHERMODE:
                phand = hand.get_cards(numerical=True)
                suggested_action = self.basic_strat.suggest_action(hhand, phand)

                print("Basic strategy says to {}".format(suggested_action))

            # determine if special actions are available for this hand?
            splittable = hand.is_splittable()
            can_double = hand.can_double()

            # query action
            action = get_game_info(self, can_double, splittable)

            # apply action
            if action == 'hit':
                self.game.hit(hand)

                # if hit causes hand to bust
                if hand.get_total_value() > 21:
                    print("{} busted!".format(player.player_identifier))
                    return

            elif action == 'stand':
                self.game.stand(hand)

            elif action == 'double' and can_double:
                self.game.double(player, hand)

            elif action == 'split' and splittable:
                hand, newhand = self.game.split(player, hand)

                # recursively play out this hand
                self.play_out_hand(player, hand)
                self.play_out_hand(player, newhand)
            else:
                print("\nEnter a valid action to take!\n")

        self.completed_hands.append(hand)

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

        # check if the house has a blackjack?
        housebj = self.game.check_dealer_blackjack()
        print("\nHouse has face up card: {}".format(self.game.house.face_up_card))

        # if house does not have a blackjack... proceed
        if housebj:
            self.game.freeze_play()
            print("Dealer has blackjack!")
        else:
            # loop through players, hands
            for player in self.game.get_players():
                for hand in player.get_hands():
                    # add all hands into the stack
                    self.in_play_hands.append((player, hand))

            while len(self.in_play_hands) != 0:
                player, hand = self.in_play_hands.pop()

                self.play_out_hand(player, hand)

        # reveal the dealer card
        self.reveal_dealer_card()

        if not housebj and len(self.completed_hands) > 0:
            # now dealer gets dealt cards
            print("Dealer is now being dealt cards...")
            self.game.stand()
            self.show_dealer_outcome()

        # reveal player cards and print out outcome of the cards
        self.reveal_player_cards()

        # determine outcomes
        self.game.determine_outcomes()

        # restart game now that we have settled
        self.restart_game()

        return 1

    def restart_game(self):
        """
        Function to restart the game, calls the game.restart() command

        :return:
        """
        for i in range(10):
            print("v\n")
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
        print("Added player {}".format(name))

    def cash_out_player(self, name):
        if self.num_players == 0:
            print("You can not remove a player if there are none!")
            return

        self.game.remove_player(name)
        self.num_players -= 1
        print("Cashed out player {}".format(name))

    def check_outcome(self):
        self.game.determine_outcomes()

    def reveal_player_cards(self):
        hhand = self.game.house.hand

        print("\n-------- Summary of game: ---------\n")
        for player in self.game.get_players():
            for idx, hand in enumerate(player.get_hands()):
                print("\nplayer: {} for hand {} had {}".format(player.player_identifier, idx + 1, hand.get_cards()))
                if hand.get_total_value() > 21:
                    print("player: {} busted, so lost!".format(player.player_identifier))
                elif hhand.get_total_value() > 21:
                    print("player: {} won!".format(player.player_identifier))
                elif hand.get_total_value() > hhand.get_total_value():
                    print("player: {} won!".format(player.player_identifier))
                elif hand.get_total_value() == hhand.get_total_value():
                    print("player: {} pushed!".format(player.player_identifier))
                else:
                    print("player: {} lost!".format(player.player_identifier))

    def reveal_dealer_card(self):
        dealer_hand = self.game.house.hand.get_cards()

        print("\nhouse: Dealer has {}.\n".format(dealer_hand))

    def show_dealer_outcome(self):
        dealer_hand = self.game.house.hand

        print("\nhouse: Dealer has {}.".format(dealer_hand.get_cards()))

        if dealer_hand.get_total_value() > 21:
            print("house: Dealer busted!")
        else:
            print("house: Dealer has {}".format(dealer_hand.get_total_value()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='BLACKJACK', description="This is the blackjack cards app made by Adam Li. \n"
                                                                   'Basic game play with '
                                                                   'optional help from a '
                                                                   'basic strategy teacher, '
                                                                   'learning agent, '
                                                                   'monte-carlo simulator, ',
                                     # 'or brute-force counter',
                                     usage="Please enter one of the following commands: \n\n"
                                           "start, add_player, help, or quit\n")
    parser.add_argument('cmd', choices=['start',
                                        'add_player',
                                        'cash_out',
                                        'help', 'quit'])

    print("\033c")
    # initialize application
    app = App()

    # print help at the beginning
    parser.print_help()
    parser.print_usage()

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

            print("\n\nNew game starting!")
            parser.print_usage()
        elif args.cmd in ['add_player']:
            player_name = get_player_info()
            app.add_player(player_name)

            parser.print_usage()
        elif args.cmd in ['cash_out']:
            player_name = get_cashout_info()
            app.cash_out_player(player_name)

            parser.print_usage()
        elif args.cmd == 'help':
            parser.print_help()

        elif args.cmd == 'quit':
            app.end_game()
            break
