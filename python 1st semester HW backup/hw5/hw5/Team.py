from Player import Player


class Team:
    def __init__(self, name, players):
        self.name = name
        self.__players = players

    def get_team(self):
        return self.__players

    def score_team(self):
        total = 0
        for i in self.__players:
            total += i.score()
        return total

    def has_dominoes_team(self):
        for i in self.__players:
            if i.has_dominoes():
                return True
            # else:
                # return False

    def play(self, board):
        for i in self.__players:
            if Player.has_dominoes(i):
                if i.play(board):
                    return True
                else:
                    continue
        else:
            return False

    def __str__(self):
        result = 'Name: ' + self.name + ',' + ' Score team: ' + str(self.score_team()) + ',' + ' Players: ' + str(self.__players)
        return result

    def __repr__(self):
        return Team.__str__(self)




