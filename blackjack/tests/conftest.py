""" Define fixtures available for blackjack game """
import os
from pathlib import Path

import pytest

from blackjack.objects.game.game import Game
from blackjack.objects.game.blackjack import PlayBlackjack

# RAWDATADIR = "/home/WIN/ali39/toshibaHDD/data/rawdata/"
# RAWDATADIR = "/Users/adam2392/Downloads/tngpipeline/"
# DATACENTERS = ['_cleveland', '_jhu', '_nih', '_ummc']


@pytest.fixture(scope='module')
def play_blackjackgame():
    # initialize the game state
    game = PlayBlackjack()

    return game

@pytest.fixture(scope='module')
def game():
    # initialize the game state
    game = Game()

    return game
