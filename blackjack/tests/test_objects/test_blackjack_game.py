import pytest


@pytest.mark.usefixture('blackjackgame')
class Test_Blackjack_Game():
    """
    Tests for the actual blackjack blackjackgame module
    """

    def test_blackjack_init(self, blackjackgame):
        # start blackjackgame
        blackjackgame.start_game()

        assert isinstance(blackjackgame.start_time, float)
        assert blackjackgame.end_time == None

        assert blackjackgame.numdecks >= 1
        assert blackjackgame.in_play == False

    def test_deal(self,blackjackgame):
        pass

    def test_hit(self, blackjackgame):
        pass

    def test_stand(self, blackjackgame):
        pass

    def test_check_blackjack(self, blackjackgame):
        # check for dealer blackjack

        # check for house blackjack
        pass

    def test_end_game(self, blackjackgame):
        blackjackgame.end_game()

        assert isinstance(blackjackgame.end_time, float)
        assert isinstance(blackjackgame.start_time, float)
