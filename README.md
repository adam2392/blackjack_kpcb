# blackjack_kpcb
A blackjack implementation using Python for the KPCB Engineering Fellow Challenge.

# Setup
Run on a Linux/MacOSx computer that has python3 and pip installed.

    # create a virtual environment
    python3 -m venv. venv
    
    # activate venv
    source .venv/bin/activate
    
    # install requirements usuing pip
    pip install -r requirements.txt
        
# Running

    python3 app.py

# App Background
I've always had a fascination with blackjack and the fact that it is a game based off of pure probability and statistics.
No matter how "lucky" you feel, or how many coincidental cards you see, the rules at the end of the day are made such that 
you will lose money in the long run no matter what. However, it is also beatable when you employ basic systems that keep
track of the game state. This was the infamous "counting" system made infamous by the MIT team (featured in the movie 21).

In this app, I build out the bare bones essentials of blackjack, incorporating all the possible
actions of the game (hit, double, stand, and split). Surrender and insurance is not taken into account because we 
impose a flat betting scheme. I also include a basic teacher in the game, that is optional to add in.

This is called basic strategy. When the player turns this on, the app will tell you exactly what you should
do based on basic strategy. This will allow you to have at most a losing edge of 49.5% vs 50.5% for the house. So
it is not bad. 

In the future, it is quite possible to extend the API to account for surrender (lose 50% of your bet automatically), insurance
(pay 50% to ensure your bet against a house blackjack) and betting minimum and maximum. 


# API Documentation
The API is documented automatically using Sphinx-doc. I will attach a documentation page made from that using the docstrings
in the code comments. Here, I will also overview at a high level my implementation strategy for the blackjack game.

Go to: https://github.com/adam2392/blackjack_kpcb/blob/master/blackjack.pdf
for a sphinx-doc api documentation.

## External Libraries/APIs:
1. pytest: for unit testing
2. pandas for easily reading in a basic strategy excel table

## High Level Split
At a high level, I split the blackjack game into:

1) configuration: a submodule to store all configurations of the game, such as number of cards in the deck. It also stores
enumerations made for the blackjack game. 
2) objects: a submodule to store the majority of the blackjack game functionality. It stores all the different objects involved in a blackjack game. Such as
the player, the house, cards, decks, hands, and the blackjack game itself.
3) teacher: this is a special submodule I made that allows users to activate the a "teacher", who will tell you what basic strategy would suggest you to do.
4) utility: this is a utility module for different functions
5) tests: this stores all the unit tests.

## Midlevel (Cards)
I represented the cards as:

1. card
2. deck
3. hand

These were three separate objects that separated functions for what a card does, what a deck does and what a hand does. The deck
contains an entire stack of cards, and interacts with the hand at a basic level of exchanging any popped cards from the deck to the hand.
The hand stores cards as a list/stack. The deck also provides the shuffle ability using the random.shuffle() function.

## Midlevel (Users)
I represented the different users as:

1. house
2. player

Since there is only one house, but multiple players, the house was relatively simple. You just need to assign one hand to the house, and it has
a pretty simple rule of hitting until it reaches 17. The players have more complex functionality, such as doubling, splitting, standing whenever the user chooses,
or hitting whenever the user chooses. The player stores the hands in a list, while also has wrappers that can reset the hands. Note, that this implies that players
can have multiple hands, while the house just has a hand, or None.

Note also that all players have a unique player identifier. This is assumed to be the case that no two players are the same.

## Midlevel (Game)
The blackjack game is probably the highest level of the objects. It is a separate object, but now interacts heavily with both users and cards. The game
stores the deck, and wraps functionality there based on blackjack game play. It also stores a reference to the House, and a dictionary of players that stores
a list of their corresponding hands. So for example, player A can have 2 hands, while player B has 1 hand. The hashmap would be an easy way of accessing all the
hands per player. Finally, the blackjack game object handles all the game play, such as dealing, hitting, standing, doubling, splitting, checking for blackjacks, and 
determining outcome of a game play.

## Wrapping It Together (app.py)
Once I wrote out the blackjack game, I then wrote the app.py file. This is just the main file that interacts with the user in the terminal. It simply
runs an infinite loop and plays out the blackjack game. Because I am familiar with the flow of the blackjack game, this was quite easy to write out 
once I had the backend sufficiently tested and modularized. 

## Testing
I chose to use pytest for my main unit testing suite because it is easy to work with, allows fixtures to be generated for a set of tests. 
I have a lot of experience with pytest, and therefore found it to be the best option.

My testing approach was to make sure that the main exceptions were raised in some of the basic object's functionality, the return states were correct
and also that certain game play produced certain results. Once this was performed, then I was satisfied that the blackjack app.py could be easily written
to just connect all the different functionalities of the blackjack api.

## Future Thoughts
A big part of learning blackjack is realizing that you just have to believe in probability and statistics. A part of the app I would be interested in extending
is overloading the OpenAI gym environment and creating an environment from my blackjack game, so that I can install a Reinforcement Learning agent that
"learns" the optimal blackjack play over time. It will be very easy to see that the agent will need to learn over a tremendous amount of play because of how
variable blackjack is. However, here we can demonstrate that a human just needs to memorize a simple hash table of what to do based on the dealer's face up card.

This makes learning optimal blackjack very easy.