from unittest import TestCase
from RandomPlayer import RandomPlayer
from Board import Board
from Domino import Domino
from Hand import Hand


class TestRandomPlayer(TestCase):
    def test_play(self):
        b1 = Board(8)
        d1 = Domino(2, 3)
        d2 = Domino(3, 6)
        d3 = Domino(5, 5)
        h1 = Hand([d1, d2, d3])
        p1 = RandomPlayer('random Batya', 80, h1)
        self.assertTrue(p1.play(b1), False)
        self.assertTrue(p1.play(b1), False)
        self.assertFalse(p1.play(b1), True)
