""" Define fixtures available for blackjack game """
import pytest

from blackjack.objects.game.game import Game
from blackjack.objects.game.deck import Deck
from blackjack.objects.game.hand import Hand
from blackjack.objects.game.blackjack import PlayBlackjack


@pytest.fixture(scope='module')
def blackjackgame():
    # initialize the game state
    game = PlayBlackjack(numdecks=1, players='johndoe', house='casino')

    return game


@pytest.fixture(scope='class')
def game():
    # initialize the game state
    game = Game()

    return game


@pytest.fixture(scope='class')
def deck():
    # initialize the game state
    deck = Deck()

    return deck


@pytest.fixture(scope='class')
def hand():
    # initialize the game state
    hand = Hand()

    return hand
