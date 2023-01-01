from Domino import Domino
from Player import Player
import copy


class MaxScorePlayer(Player):
    def __init__(self, name, age, hand):
        Player.__init__(self, name, age, hand)

    def play(self, board):
        lst = copy.copy(self.hand.array)
        lst2 = sorted(lst, reverse=True)
        for i in lst2:
            if board.add(i):
                self.hand.remove_domino(i)
                return True
        else:
            return False

    def __str__(self):
        result = 'Name: ' + self.name + ',' + ' Age: ' + str(self.age) + ',' + ' Hand: ' + str(
            self.hand) + ',' + ' Score: ' + str(self.score()) + ',' + ' I can win the game!'
        return result

    def __repr__(self):
        return MaxScorePlayer.__str__(self)
