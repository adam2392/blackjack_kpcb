""" Define fixtures available for blackjack cards """
import pytest

from blackjack.objects.game.blackjack import PlayBlackjack
from blackjack.objects.cards.deck import Deck
from blackjack.objects.game.game import Game
from blackjack.objects.cards.hand import Hand
from blackjack.objects.users.player import Player


@pytest.fixture(scope='module')
def blackjackgame():
    # initialize the cards state
    game = PlayBlackjack(numdecks=1)

    return game


@pytest.fixture(scope='class')
def game():
    # initialize the cards state
    game = Game()

    return game


@pytest.fixture(scope='class')
def deck():
    # initialize the cards state
    deck = Deck()

    return deck


@pytest.fixture(scope='class')
def hand():
    # initialize the cards state
    hand = Hand()

    return hand


@pytest.fixture(scope='class')
def player():
    # initialize the cards state
    player = Player("John doe")

    return player
