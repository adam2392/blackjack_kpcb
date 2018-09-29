import argparse

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

    return name


def get_game_info():
    parser = argparse.ArgumentParser(prog='BLACKJACK',
                                     usage="\nPlease enter one of the following commands to proceed: \n"
                                           "hit, double, split, stand, help, or quit")
    parser.add_argument('cmd', choices=['hit', 'double',
                                        'split', 'stand',
                                        'help', 'quit'])
    parser.print_usage()

    while True:
        astr = input('$: ')

        try:
            args = parser.parse_args(astr.split())
        except SystemExit:
            # trap argparse error message
            print('error please enter a valid command')
            continue
        if args.cmd == 'help':
            parser.print_help()

        elif args.cmd == 'quit':
            app.end_game()
            return "quit"

        action = args.cmd
        break

    return action
