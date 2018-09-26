import pytest

from blackjack.objects.game.deck import Deck


@pytest.mark.usefixture('hand')
class Test_Hand():
    """
    Tests for the game module that has basic functionality of a deck.
    """

    def test_hand(self, hand):
        # test the initial hand
        assert hand.cards == []
        assert hand.get_value() == 0
        assert hand.get_soft_value() == 0

        # now add cards and see
        deck = Deck()
        deck.shuffle()
        card = deck.deal_card()
        hand.add_card(card)

        # check value of the hand with 10s vs other
        if card.get_rank() < 10:
            assert hand.get_value() == card.get_rank()
        # check value of the card with an Ace
        elif card.get_rank() == 1:
            assert hand.get_soft_value() == 11
        else:
            assert hand.get_value() <= card.get_rank()

        # now add cards and see
        deck = Deck()
        deck.shuffle()
        card = deck.deal_card()
        hand.add_card(card)
        # test soft hands return greater then value hands
        while hand.get_value() < 21 and hand.get_soft_value() < 21:
            card = deck.deal_card()
            hand.add_card(card)
            if card.get_rank() == 1:
                break
            # else:
            #     assert hand.get_value() == hand.get_soft_value()

        assert hand.get_value() <= hand.get_soft_value()
