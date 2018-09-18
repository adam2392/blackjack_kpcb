import os
import pandas as pd

basedir = os.path.abspath(__file__)
basedir = os.path.expanduser("~/Documents/blackjack_kpcb")
BASICSTRATEGY_FILEPATH = os.path.join(basedir, "blackjack/config/basic_strategy.xlsx")


class BasicStrategy(object):
    strategy = None

    def __init__(self):
        self.datafile = BASICSTRATEGY_FILEPATH

        print(self.datafile)
        # build out the hashmap
        self._build_hash_map()

    def _build_hash_map(self):
        strat_map = pd.read_excel(self.datafile, header=None, index_col=None, names=None)

        print(strat_map.head())

    def get_action(self, hash_cards):
        """
        Function to return the action suggested by this strategy
        for the combination of cards, a player has.

        :param hash_cards:
        :return:
        """

        assert len(hash_cards) == 3
        player_total = sum(hash_cards[0:2])
        house_up = hash_cards[2]

        # not able to split
        if hash_cards[0] != hash_cards[1]:
            action = self.strategy[player_total][house_up]

            assert action in ['s', 'su', 'd', 'h']
        # if we can split, let us determine if we can do that
        else:
            player_card = hash_cards[0]
            action = self.strategy[player_card][house_up]

            assert action in ['s', 'su', 'sp', 'd', 'h']
        return action

if __name__ == '__main__':
    basicstrategy = BasicStrategy()
