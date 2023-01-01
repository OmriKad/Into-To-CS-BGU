from unittest import TestCase
from Domino import Domino
from Hand import Hand
from Player import Player
from Board import Board


class TestPlayer(TestCase):
    def test_score(self):
        d1 = Domino(2, 3)
        d2 = Domino(4, 6)
        h1 = Hand([d1, d2])
        p1 = Player('susu', 88, h1)
        self.assertEqual(p1.score(), 15)

    def test_play(self):
        b1 = Board(8)
        d1 = Domino(2, 3)
        h1 = Hand([d1])
        p1 = Player('susu', 88, h1)
        self.assertEqual(p1.play(b1), None)

    def test_has_dominoes(self):
        d1 = Domino(2, 3)
        h1 = Hand([d1])
        p1 = Player('susu', 88, h1)
        self.assertTrue(p1.has_dominoes(), False)
        h1.remove_domino(d1)
        self.assertFalse(p1.has_dominoes(), True)

    def test_str_repr(self):
        d1 = Domino(2, 3)
        h1 = Hand([d1])
        p1 = Player('susu', 88, h1)
        self.assertEqual(str(p1), "Name: susu, Age: 88, Hand: [2|3], Score: 5")
        self.assertEqual(repr(p1), "Name: susu, Age: 88, Hand: [2|3], Score: 5")

