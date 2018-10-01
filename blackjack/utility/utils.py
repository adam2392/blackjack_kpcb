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


def get_game_info(app, can_double, splittable):
    if splittable:
        cmd_choices = ['hit', 'double',
                       'split', 'stand',
                       'help']
        usage_str = "hit, stand, (optional) double, (optional) split, or help."
    elif not splittable and can_double:
        cmd_choices = ['hit', 'double', 'stand',
                       'help']
        usage_str = "hit, stand, (optional) double, or help."
    else:
        cmd_choices = ['hit', 'stand',
                       'help']
        usage_str = "hit, stand, or help."

    parser = argparse.ArgumentParser(prog='BLACKJACK',
                                     usage="\nPlease enter one of the following commands to proceed: \n"
                                           + usage_str)
    parser.add_argument('cmd', choices=cmd_choices)
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

        else:
            action = args.cmd
            break

    return action
