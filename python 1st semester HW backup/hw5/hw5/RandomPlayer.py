import random
import copy
from Player import Player


class RandomPlayer(Player):
    def play(self, board):
        # Don't change this line and don't move it!
        random.seed(12)  # You can read about seed here: https://en.wikipedia.org/wiki/Random_seed
        # TODO: write your code after this line
        lst = copy.copy(self.hand.array)
        random.shuffle(lst)
        for i in lst:
            if i is not None:
                if board.add(i):
                    self.hand.remove_domino(i)
                    return True







