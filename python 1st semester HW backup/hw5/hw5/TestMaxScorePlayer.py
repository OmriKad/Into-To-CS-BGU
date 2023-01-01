from unittest import TestCase
from Board import Board
from Domino import Domino
from Hand import Hand
from MaxScorePlayer import MaxScorePlayer


class TestMaxScorePlayer(TestCase):
    def test_play(self):
        b1 = Board(8)
        d1 = Domino(1, 1)
        d2 = Domino(3, 5)
        d3 = Domino(5, 5)
        h1 = Hand([d1, d2, d3])
        p1 = MaxScorePlayer('yechezkel the ace', 99, h1)
        self.assertTrue(p1.play(b1), False)
        self.assertTrue(p1.play(b1), False)
        self.assertFalse(p1.play(b1), True)

    def test_str_repr(self):
        b1 = Board(8)
        d1 = Domino(2, 3)
        d2 = Domino(3, 6)
        d3 = Domino(5, 5)
        h1 = Hand([d1, d2, d3])
        p1 = MaxScorePlayer('yechezkel the ace', 99, h1)
        self.assertEqual(str(p1), "Name: yechezkel the ace, Age: 99, Hand: [2|3][3|6][5|5], Score: 24, I can win the game!")
        self.assertEqual(repr(p1), "Name: yechezkel the ace, Age: 99, Hand: [2|3][3|6][5|5], Score: 24, I can win the game!")
