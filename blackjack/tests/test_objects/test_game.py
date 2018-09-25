import pytest
# from blackjack.objects.game.game import Game

@pytest.mark.usefixture('game')
class Test_Game():

    def test_start_game(self, game):
        assert game.start_time == None
        assert game.end_time == None

        game.start_game()

        assert isinstance(game.start_time, float)
        assert game.end_time == None

    def test_end_game(self, game):
        assert game.start_time == None
        assert game.end_time == None

        game.end_game()

        assert isinstance(game.end_time, float)
        assert game.start_time == None