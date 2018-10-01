from blackjack.teacher.base import BaseTeacher


class Counter(BaseTeacher):

    def __init__(self):
        self.intelligence = 10

    def description(self):
        print("A perfect counter that keeps track of the running count and true count!")

    def suggest_action(self, house, players):
        """
        Counter suggest action based on the true count.

        Uses a hard-coded hash table of suggested actions
        based on optimal blackjack actions.

        :param house:
        :param players:
        :return:
        """
        pass
