import pytest

from blackjack.objects.users.player import Player


@pytest.mark.usefixture('blackjackgame')
class Test_Blackjack_Funcs():
    """
    Tests for the actual blackjack blackjackgame module's basic functions
    """

    def test_blackjack_init(self, blackjackgame):
        # start blackjackgame
        blackjackgame.start_game()

        assert isinstance(blackjackgame.start_time, float)
        assert blackjackgame.end_time == None

        assert blackjackgame.numdecks >= 1
        assert blackjackgame.in_play == False

    def test_add_player(self, blackjackgame):
        player = Player("John Doe", "18", "500")
        blackjackgame.add_player(player)

        assert isinstance(blackjackgame.players, dict)
        assert blackjackgame.players[player.player_identifier] == player

        with pytest.raises(ValueError):
            blackjackgame.add_player(player)

        with pytest.raises(TypeError):
            blackjackgame.add_player("hi")

        # add another player in here to make sure we have both
        player = Player("John Doe", "18", "501")
        blackjackgame.add_player(player)

    def test_remove_player(self, blackjackgame):
        player = Player("John Doe", "18", "500")
        blackjackgame.remove_player(player)

        with pytest.raises(ValueError):
            blackjackgame.remove_player("hi")

    def test_place_bets(self, blackjackgame):
        bet = 100

        for player in blackjackgame.get_players():
            player.place_bet(bet)

            assert player.get_total_bet() == bet

    def test_restart(self, blackjackgame):
        blackjackgame.restart()

        assert blackjackgame.in_play == False
        assert blackjackgame.house.hand == None

        for player in blackjackgame.get_players():
            for hand in player.get_hands():
                assert hand == []

    def test_end_game(self, blackjackgame):
        blackjackgame.end_game()

        assert isinstance(blackjackgame.end_time, float)
        assert isinstance(blackjackgame.start_time, float)
