import pytest

from blackjack.teacher.base import BasicStrategyTeacher
from blackjack.objects.users.player import Player


@pytest.mark.usefixtures("blackjackgame")
class Test_BasicStrategy():

    def test_bs(self, blackjackgame):
        bs = BasicStrategyTeacher()

        # add another player in here to make sure we have both
        player = Player("John Doe")
        blackjackgame.add_player(player)

        # bet = 100
        # for player in blackjackgame.get_players():
        #     player.place_bet(bet)
        #     assert player.get_total_bet() == bet

        # deal the blackjack
        blackjackgame.deal()

        for player in blackjackgame.get_players():
            for phand in player.get_hands():
                action = bs.suggest_action(blackjackgame.house.hand, phand)


                print(blackjackgame.house.hand, phand, action)

