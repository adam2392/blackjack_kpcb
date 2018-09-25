import pytest

from blackjack.objects.users.house import House
from blackjack.objects.users.player import Player

class Test_House():
    def test_house(self):
        house = House()

        assert isinstance(str(house), str)
        assert isinstance(house.bankroll, float)

class Test_Player():
    def test_player(self):
        player = Player()