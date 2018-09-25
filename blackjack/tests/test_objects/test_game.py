import pytest


@pytest.mark.usefixture('game')
class Test_Game():
    """
    Tests for the game module that has basic functionality of games.
    """

    def test_start_game(self, game):
        # assert game.start_time == None
        # assert game.end_time == None

        game.start_game()

        assert isinstance(game.start_time, float)
        assert game.end_time == None

    def test_end_game(self, game):
        # assert isinstance(game.start_time, float)
        # assert game.end_time == None

        game.end_game()

        assert isinstance(game.end_time, float)
        assert isinstance(game.start_time, float)
