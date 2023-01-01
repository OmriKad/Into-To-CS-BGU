from unittest import TestCase
from Team import Team
from Player import Player
from NaivePlayer import NaivePlayer
from Board import Board
from MaxScorePlayer import MaxScorePlayer
from RandomPlayer import RandomPlayer
from Domino import Domino
from Hand import Hand


class TestTeam(TestCase):
    def test_get_team(self):
        b1 = Board(8)
        d1 = Domino(1, 1)
        d2 = Domino(3, 5)
        d3 = Domino(5, 5)
        h1 = Hand([d1])
        h2 = Hand([d2])
        h3 = Hand([d3])
        p1 = MaxScorePlayer('yechezkel the ace', 99, h1)
        p2 = NaivePlayer('susu', 84, h2)
        p3 = RandomPlayer('sasa', 84, h3)
        t1 = Team('Beit avot 1', [p1, p2, p3])
        self.assertEqual(t1.get_team(), [p1, p2, p3])

    def test_score_team(self):
        d1 = Domino(1, 1)
        d2 = Domino(3, 5)
        d3 = Domino(5, 5)
        h1 = Hand([d1])
        h2 = Hand([d2])
        h3 = Hand([d3])
        p1 = MaxScorePlayer('yechezkel the ace', 99, h1)
        p2 = NaivePlayer('susu', 84, h2)
        p3 = RandomPlayer('sasa', 84, h3)
        t1 = Team('Beit avot 1', [p1, p2, p3])
        self.assertEqual(t1.score_team(), 20)

    def test_has_dominoes_team(self):
        d1 = Domino(1, 1)
        d2 = Domino(3, 5)
        d3 = Domino(5, 5)
        h1 = Hand([d1])
        h2 = Hand([d2])
        h3 = Hand([d3])
        p1 = MaxScorePlayer('yechezkel the ace', 99, h1)
        p2 = NaivePlayer('susu', 84, h2)
        p3 = RandomPlayer('sasa', 84, h3)
        t1 = Team('Beit avot 1', [p1, p2, p3])
        t2 = Team('Beit avot 1', [])
        self.assertTrue(t1.has_dominoes_team(), False)
        self.assertFalse(t2.has_dominoes_team(), True)

    def test_play(self):
        b1 = Board(8)
        d1 = Domino(1, 1)
        d2 = Domino(3, 5)
        d3 = Domino(5, 5)
        h1 = Hand([d1])
        h2 = Hand([d2])
        h3 = Hand([d3])
        p1 = MaxScorePlayer('yechezkel the ace', 99, h1)
        p2 = NaivePlayer('susu', 84, h2)
        p3 = RandomPlayer('sasa', 84, h3)
        t1 = Team('Beit avot 1', [p3, p2, p1])

        #self.assertTrue(t1.play(b1), False)
        #self.assertTrue(t1.play(b1), False)
        #self.assertFalse(t1.play(b1), True)

    def test_str_repr(self):
        d1 = Domino(1, 1)
        d2 = Domino(3, 5)
        d3 = Domino(5, 5)
        h1 = Hand([d1])
        h2 = Hand([d2])
        h3 = Hand([d3])
        p1 = MaxScorePlayer('yechezkel the ace', 99, h1)
        p2 = NaivePlayer('susu', 84, h2)
        p3 = RandomPlayer('sasa', 84, h3)
        t1 = Team('Beit avot 1', [p1, p2, p3])
        self.assertEqual(str(t1), "Name: Beit avot 1, Score team: 20, Players: [Name: yechezkel the ace, Age: 99, Hand: [1|1], Score: 2, I can win the game!, Name: susu, Age: 84, Hand: [3|5], Score: 8, Name: sasa, Age: 84, Hand: [5|5], Score: 10]")
        self.assertEqual(repr(t1), "Name: Beit avot 1, Score team: 20, Players: [Name: yechezkel the ace, Age: 99, Hand: [1|1], Score: 2, I can win the game!, Name: susu, Age: 84, Hand: [3|5], Score: 8, Name: sasa, Age: 84, Hand: [5|5], Score: 10]")
