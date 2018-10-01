import os
import pandas as pd
import re

import blackjack
from blackjack.config.enum.actions import Actions
from blackjack.config import params

basedir = os.path.dirname(blackjack.__file__)
basedir = os.path.dirname(os.path.abspath(__file__))
basedir = os.path.join(basedir, '..')
BASICSTRATEGY_FILEPATH = os.path.join(basedir, "config/basic_strategy.xlsx")


class BasicStrategy(object):
    def __init__(self):
        self.datafile = BASICSTRATEGY_FILEPATH

        # build out the hashmap
        self.strategymap = self._build_hash_map()

    def _build_hash_map(self):
        """
        Helper function to build up the cleaned up dataframe from the basic strategy
        excel sheet.
        :return:
        """
        strat_map = pd.read_excel(self.datafile, index_col=None, names=None)

        # do some string modification of the strategy head
        strat_map.index = strat_map.index.str.replace(',', '').str.replace(' ', '')
        strat_map = strat_map.rename(columns=lambda x: re.sub(',', '', x))
        for col in strat_map.columns.values:
            strat_map[col].apply(lambda x: x.replace(',', ''))

        return strat_map

    def get_action(self, hash_cards):
        """
        Function to return the action suggested by this strategy
        for the combination of cards, a player has.

        :param hash_cards:
        :return: an action in the space
        """

        assert len(hash_cards) == 3
        # extract total from player card
        player_total = sum(hash_cards[0:2])

        # extract player cards
        player_cards = hash_cards[0:2]
        player_cards.sort()
        player_cards = [str(i) for i in player_cards]

        # extract house card
        house_up = str(hash_cards[2])

        # map house up card from 1 to Ace
        if house_up == "1":
            house_up = 'A'

        # if user does not have ace & it is below 9
        if "1" not in player_cards and player_total < 9:
            action = Actions.hit.value

        elif player_total >= 17:
            action = Actions.stand.value

        elif "1" in player_cards:
            if "1" == player_cards[1]:
                rowval = ''.join(['A', 'A'])
            else:
                rowval = ''.join(['A', player_cards[1]])
            action = self.strategymap.loc[rowval, house_up]

        # if we can split, let us determine if we can do that
        elif player_cards[0] == player_cards[1]:
            rowval = ''.join(player_cards)
            action = self.strategymap.loc[rowval, house_up]
        else:
            rowval = str(player_total)
            action = self.strategymap.loc[rowval, house_up]

        print(action.lower())
        assert action.lower() in params.action_space
        return action.lower()


if __name__ == '__main__':
    basicstrategy = BasicStrategy()

    print(basicstrategy.get_action([1, 1, 1]))
    print(basicstrategy.get_action([1, 2, 2]))
    print(basicstrategy.get_action([1, 1, 10]))
    print(basicstrategy.get_action([4, 5, 4]))
