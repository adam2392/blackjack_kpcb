import pytest


@pytest.mark.usefixture('cards')
class Test_Game():
    """
    Tests for the cards module that has basic functionality of games.
    """

    def test_start_game(self, game):
        # assert cards.start_time == None
        # assert cards.end_time == None

        game.start_game()

        assert isinstance(game.start_time, float)
        assert game.end_time == None

    def test_end_game(self, game):
        # assert isinstance(cards.start_time, float)
        # assert cards.end_time == None

        game.end_game()

        assert isinstance(game.end_time, float)
        assert isinstance(game.start_time, float)
