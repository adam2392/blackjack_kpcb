import pytest

from blackjack.objects.users.player import Player


@pytest.mark.usefixture("blackjackgame")
class Test_Blackjack_Game():
    """
    Class of tests to test actual cards play under some explicit scenarios

    """

    def test_blackjack_init(self, blackjackgame):
        # start blackjackgame
        blackjackgame.start_game()

        assert isinstance(blackjackgame.start_time, float)
        assert blackjackgame.end_time == None

        assert blackjackgame.numdecks >= 1
        assert blackjackgame.in_play == False

        player = Player("John Doe")
        blackjackgame.add_player(player)

        assert isinstance(blackjackgame.players, dict)
        assert blackjackgame.players[player.player_identifier] == player

        # add another player in here to make sure we have both
        player = Player("John Doe01")
        blackjackgame.add_player(player)

    def test_add_player(self,blackjackgame):
        # add another player in here to make sure we have both
        player = Player("John Doe92")
        blackjackgame.add_player(player)

        with pytest.raises(ValueError):
            blackjackgame.add_player(player)

        with pytest.raises(TypeError):
            blackjackgame.add_player("hi")

    def test_place_bets(self, blackjackgame):
        pass
        # bet = 100
        # for player in blackjackgame.get_players():
        #     player.place_bet(bet)
        #
        #     assert player.get_total_bet() == bet

    def test_deal(self, blackjackgame):
        # clean start the blackjack
        blackjackgame.restart()

        # bet = 100
        # for player in blackjackgame.get_players():
        #     player.place_bet(bet)
            # assert player.get_total_bet() == bet

        blackjackgame.deal()

        # assert each hand starts off with 2 cards
        assert len(blackjackgame.house.hand.get_cards()) == 2
        assert blackjackgame.house.hand.get_soft_value() <= 21 and blackjackgame.house.hand.get_value() <= 20

        for player in blackjackgame.get_players():
            for hand in player.get_hands():
                assert len(hand.get_cards()) == 2
                assert hand.get_soft_value() <= 21 and hand.get_value() <= 20

    def test_check_blackjack(self, blackjackgame):
        # check for dealer blackjack
        bj = blackjackgame.check_dealer_blackjack()

        if bj:
            assert blackjackgame.house.hand.get_soft_value() == 21
        else:
            assert blackjackgame.house.hand.get_soft_value() < 21

        # check for house blackjack
        for player in blackjackgame.get_players():
            for hand in player.get_hands():
                bj = blackjackgame.check_player_blackjack(hand)

                if bj:
                    assert blackjackgame.house.hand.get_soft_value() == 21
                else:
                    assert blackjackgame.house.hand.get_soft_value() < 21

    def test_hit(self, blackjackgame):
        for i in range(100):
            for player in blackjackgame.get_players():
                for hand in player.get_hands():
                    if hand.can_hit():
                        blackjackgame.hit(hand)
                    else:
                        assert hand.get_value() >= 21

    def test_stand(self, blackjackgame):
        for i in range(100):
            for player in blackjackgame.get_players():
                for hand in player.get_hands():
                    if hand.can_hit():
                        blackjackgame.hit(hand)
                    else:
                        assert hand.get_value() >= 21

        for player in blackjackgame.get_players():
            for hand in player.get_hands():
                blackjackgame.stand(hand)

        assert blackjackgame.in_play == True

        blackjackgame.stand()

        assert blackjackgame.in_play == False
        assert blackjackgame.house.hand.get_value() >= 17 or blackjackgame.house.hand.get_soft_value() >= 17

    def test_determine_outcomes(self, blackjackgame):
        # clean start the blackjack
        blackjackgame.restart()

        # bet = 100
        # for player in blackjackgame.get_players():
        #     player.place_bet(bet)
        #     assert player.get_total_bet() == bet

        # deal the blackjack
        blackjackgame.deal()

        # assert each hand starts off with 2 cards
        assert len(blackjackgame.house.hand.get_cards()) == 2
        assert blackjackgame.house.hand.get_soft_value() <= 21 and blackjackgame.house.hand.get_value() <= 20

        for player in blackjackgame.get_players():
            for hand in player.get_hands():
                assert len(hand.get_cards()) == 2
                assert hand.get_soft_value() <= 21 and hand.get_value() <= 20

        for i in range(100):
            for player in blackjackgame.get_players():
                for hand in player.get_hands():
                    if hand.can_hit():
                        blackjackgame.hit(hand)
                    else:
                        assert hand.get_value() >= 21

        for player in blackjackgame.get_players():
            for hand in player.get_hands():
                blackjackgame.stand(hand)

        assert blackjackgame.in_play == True

        blackjackgame.stand()

        blackjackgame.determine_outcomes()
