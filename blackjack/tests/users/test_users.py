import pytest
from blackjack.objects.users.house import House
from blackjack.objects.cards.hand import Hand

class Test_House():
    def test_house(self):
        house = House()

        assert isinstance(str(house), str)
        # assert isinstance(house.bankroll, float)


@pytest.mark.usefixture('player')
class Test_Player():
    def test_player(self, player):
        assert isinstance(player.player_identifier, str)

    def test_deal_hand(self, player):
        with pytest.raises(RuntimeError):
            for i in range(5):
                hand = Hand()
                player.deal_hand(hand)

    def test_get_hands(self,player):
        assert isinstance(player.get_hands(), list)

