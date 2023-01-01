from Domino import Domino


class Player:
    def __init__(self, name, age, hand):
        self.name = name
        self.age = age
        self.hand = hand

    def score(self):
        sum = 0
        for i in self.hand:
            if i is None:
                break
            sum += int(Domino.get_left(i)) + int(Domino.get_right(i))
        return sum

    def has_dominoes(self):
        if not self.hand:
            return False
        else:
            return True

    def play(self, board):
        pass

    def __str__(self):
        result = 'Name: ' + self.name + ',' + ' Age: ' + str(self.age) + ',' + ' Hand: ' + str(
            self.hand) + ',' + ' Score: ' + str(self.score())
        return result

    def __repr__(self):
        return Player.__str__(self)
