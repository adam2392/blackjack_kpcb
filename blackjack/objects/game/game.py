import time

class Game(object):
    start_time = None
    end_time = None

    def __init__(self):
        self.start_time = time.time()
