from abc import ABC, abstractmethod
from blackjack.config.params import action_descript, action_space

class BaseTeacher(metaclass=ABC):
    # intelligence level (easy, medium, hard) of the teacher
    # or 0 - 10
    intelligence = None

    def __str__(self):
        return str(self.__class__)

    def __repr__(self):
        print(self.__class__)

    @abstractmethod
    def suggest_action(self, house, players):
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
    def suggest_action(self, house, player):
        # get the house face up card
        house_face_up = house.face_up

        # get the player card
        player_starting = player.cards[0:2]

        # apply hash map of player cards vs house faceup
        hash_cards = player_starting.extend(house_face_up)

        suggested_action = basic_strategy.get_action(hash_cards)

    def description(self):
        print("Suggests actions based on basic strategy. Note House edge vs player is 51/49%.")
