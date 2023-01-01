from Player import Player


class NaivePlayer(Player):
    def __init__(self, name, age, hand):
        Player.__init__(self, name, age, hand)

    def play(self, board):
        for i in self.hand:
            if i is None:
                return False
            if board.add(i):
                self.hand.remove_domino(i)
                return True










