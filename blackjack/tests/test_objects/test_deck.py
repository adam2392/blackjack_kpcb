import pytest

from blackjack.objects.cards.deck import Card


@pytest.mark.usefixture('deck')
class Test_Deck():
    """
    Tests for the cards module that has basic functionality of a deck.
    """

    def test_deck(self, deck):
        # deck has to have 52 card multiples
        assert deck.numcards % 52 == 0
        assert len(deck) == deck.numcards

    def test_shuffle(self, deck):
        orig_deck = deck.cards.copy()
        deck.shuffle()
        new_deck = deck.cards

        assert not all(orig_deck[ind] == new_deck[ind] for ind in range(len(orig_deck)))
        assert len(orig_deck) == len(new_deck)

    def test_deal_card(self, deck):
        all_cards = set()
        for i in range(len(deck)):
            val = str(deck.deal_card())
            if val not in all_cards:
                all_cards.add(val)
            else:
                assert False
        assert True


class Test_Card():
    def test_card(self):
        card = Card()
        highcard = Card(0, 3)

        assert card < highcard

        highcard = Card(1)
        assert card < highcard

        highcard = Card(0, 2)
        assert card == highcard
