from abc import ABC, abstractmethod
import pandas as pd

from blackjack.config import params
from blackjack.objects.users.player import Player
from blackjack.objects.users.house import House

from blackjack.config.params import action_descript, action_space

class BaseTeacher(ABC):
    # intelligence level (easy, medium, hard) of the teacher
    # or 0 - 10
    # intelligence = None

    # def __str__(self):
    #     return str(self.__class__)
    #
    # def __repr__(self):
    #     print(self.__class__)

    @abstractmethod
    def suggest_action(self):
        """
        Function that suggests an action based on the
        current state of the game.

        Most learners will have the ability to process
        and remember previous game state information by nature
        of their models.

        :param house:
        :param players:
        :return:
        """
        pass

    @abstractmethod
    def description(self):
        pass

class BasicStrategy(BaseTeacher):
    def __init__(self):
        basic_strategy = pd.read_excel(params.STRATEGYFILE)
        print(basic_strategy)
        self.basic_strategy = basic_strategy

    def suggest_action(self, house, player):
        # get the house face up card
        house_face_up = house.get_cards()[0:1]

        # get the player card
        player_starting = player.cards[0:2]

        # apply hash map of player cards vs house faceup
        hash_cards = player_starting.extend(house_face_up)

        suggested_action = self.get_action(hash_cards)

    def get_action(self, hash):
        return self.basic_strategy_map[hash]

    def description(self):
        print("Suggests actions based on basic strategy. Note House edge vs player is 51/49%.")
