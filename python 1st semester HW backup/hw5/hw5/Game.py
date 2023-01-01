from Team import Team


class Game:
    def __init__(self, board, team1, team2):
        self.board = board
        self.team1 = team1
        self.team2 = team2

    def play(self):
        """
        This method eminences the game by its rules. With each team taking a turn until they stuck,only when the 2 teams
        get stuck, the loop breaks and the scores can be count.
        :return:
        """
        t1_stuck = 0
        t2_stuck = 0
        while t1_stuck != 2 and t2_stuck != 2:
            while Team.has_dominoes_team(self.team1):
                if Team.score_team(self.team1) == 0:
                    return str('Team ' + str(self.team1.name) + ' wins Team ' + str(self.team2.name))
                elif Team.play(self.team1, self.board):
                    t1_stuck = 0
                    continue
                else:
                    t1_stuck += 1
                    break

            while Team.has_dominoes_team(self.team2):
                if Team.score_team(self.team2) == 0:
                    return str('Team ' + str(self.team2.name) + ' wins Team ' + str(self.team1.name))
                if Team.play(self.team2, self.board):
                    t2_stuck = 0
                    continue
                else:
                    t2_stuck += 1
                    break

        if Team.score_team(self.team1) < Team.score_team(self.team2):
            return str('Team ' + str(self.team1.name) + ' wins Team ' + str(self.team2.name))
        elif Team.score_team(self.team2) < Team.score_team(self.team1):
            return str('Team ' + str(self.team2.name) + ' wins Team ' + str(self.team1.name))
        elif Team.score_team(self.team1) == Team.score_team(self.team2):
            return str('Draw!')


