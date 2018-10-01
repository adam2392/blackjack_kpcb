import time


class Game(object):
    def __init__(self):
        self.start_game()
        self.end_time = None

    def start_game(self):
        self.start_time = time.time()

    def end_game(self):
        self.end_time = time.time()
        print("You played for {:.2f} seconds".format(self.end_time - self.start_time))

