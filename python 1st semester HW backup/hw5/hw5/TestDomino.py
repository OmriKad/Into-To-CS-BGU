from unittest import TestCase
from Domino import Domino
from Exceptions import InvalidNumberException


class TestDomino(TestCase):
    def test_get_left(self):
        d = Domino(1, 2)
        self.assertEqual(d.get_left(), 1)

    def test_get_right(self):
        d = Domino(1, 2)
        self.assertEqual(d.get_right(), 2)

    def test_flip(self):
        d = Domino(1, 2)
        self.assertEqual(d.flip(), Domino(2, 1))

    def test_str_Domino(self):
        d = Domino(1, 2)
        self.assertEqual(str(d), '[1|2]')
        self.assertRaises(InvalidNumberException, Domino, 2, 7)

    def test_repr_Domino(self):
        d = Domino(1, 2)
        self.assertEqual(repr(d), '[1|2]')

    def test_gt_Domino(self):
        d = Domino(1, 2)
        d1 = Domino(3, 2)
        d2 = Domino(1, 1)
        self.assertEqual(d1.__gt__(d), True)
        self.assertEqual(d2.__gt__(d), False)

    def test_eq_Domino(self):
        d = Domino(1, 2)
        d1 = Domino(2, 1)
        d2 = Domino(4, 4)
        self.assertEqual(d.__eq__(d1), True)
        self.assertEqual(d.__eq__(d2), False)

    def test_ne_Domino(self):
        d = Domino(1, 2)
        d1 = Domino(3, 1)
        d2 = Domino(2, 1)
        self.assertEqual(d.__ne__(d1), True)
        self.assertEqual(d.__ne__(d2), False)

    def test_contains_Domino(self):
        d = Domino(1, 2)
        self.assertEqual(d.__contains__(1), True)
        self.assertEqual(d.__contains__(4), False)
