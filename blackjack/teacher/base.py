from abc import ABC, abstractmethod
from blackjack.utility.strategy import BasicStrategy


class BaseTeacher(ABC):

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


class BasicStrategyTeacher(BaseTeacher):
    def __init__(self):
        self.teacher = BasicStrategy()

    def suggest_action(self, hhand, phand):
        # get the house face up card
        house_face_up = hhand.get_cards(numerical=True)[0:1]

        # get the player card
        player_starting = phand.get_cards(numerical=True)[0:2]

        # apply hash map of player cards vs house faceup
        hash_cards = player_starting
        hash_cards.extend(house_face_up)

        return self.teacher.get_action(hash_cards)

    def description(self):
        print("Suggests actions based on basic strategy. "
              "Note House edge vs player is 51/49%.")
