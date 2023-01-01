from unittest import TestCase
from Board import Board
from Domino import Domino
from Hand import Hand
from NaivePlayer import NaivePlayer


class TestNaivePlayer(TestCase):
    def test_play(self):
        b1 = Board(8)
        d1 = Domino(2, 3)
        d2 = Domino(1, 1)
        d3 = Domino(6, 2)
        h1 = Hand([d1, d2])
        p1 = NaivePlayer('susu', 88, h1)
        self.assertTrue(p1.play(b1), False)
        self.assertFalse(p1.play(b1), True)
        self.assertFalse(p1.play(b1), True)



