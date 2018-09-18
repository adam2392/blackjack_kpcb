# default configuration settings for the blackjack game

NUMCARDS_IN_DECK = 52
BURN_CARD = 0
SURRENDER = True
INSURANCE = True
DEALER_HITS_SEVENTEEN = True
MAX_SPLIT = 4

NUMDECKS = 1

# action space of the game per player
action_space = ['b', 'h', 's', 'sp', 'su', 'd', 'i']
action_descript = {
    'b': 'Bet (how much $ to place for this hand)',
    'h': 'Hit (one more card)',
    's': 'Stand',
    'sp': 'Split',
    'su': 'Surrender (get 50% of your bet returned)',
    'd': 'Double (apply <= 100% of your bet for only one more card)',
    'i': 'Insurance (apply <= 50% of your bet to insure your bet against a house blackjack)'
}
