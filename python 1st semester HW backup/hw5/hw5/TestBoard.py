from unittest import TestCase
from Collection import Collection
from Board import Board
from Domino import Domino
from Exceptions import InvalidNumberException, EmptyBoardException, FullBoardException


class TestBoard(TestCase):
    def test_max_capacity(self):
        self.assertRaises(InvalidNumberException, Board, 29)
        self.assertRaises(InvalidNumberException, Board, -1)

    def test_Board(self):
        """ Test for str, len, repr and add """
        b = Board(5)
        d1 = Domino(3, 5)
        d2 = Domino(5, 6)
        d3 = Domino(1, 6)
        d4 = Domino(2, 3)
        d5 = Domino(2, 4)
        d6 = Domino(1, 1)
        d7 = Domino(6, 6)

        self.assertTrue(b.add(d1), False)
        self.assertEqual(str(b), '[3|5]')
        self.assertEqual(len(b), 1)
        self.assertTrue(b.add(d2), False)
        self.assertEqual(str(b), '[3|5][5|6]')
        self.assertTrue(b.add(d3), False)
        self.assertEqual(str(b), '[3|5][5|6][6|1]')
        self.assertTrue(b.add(d4), False)
        self.assertEqual(str(b), '[2|3][3|5][5|6][6|1]')
        self.assertFalse(b.add(d7), True)
        self.assertTrue(b.add(d5), False)
        self.assertEqual(str(b), '[4|2][2|3][3|5][5|6][6|1]')
        self.assertRaises(FullBoardException, b.add, d6)
        self.assertEqual(repr(b), '[4|2][2|3][3|5][5|6][6|1]')

    def test_in_right_empty(self):
        b = Board(8)
        self.assertRaises(EmptyBoardException, b.in_right)

    def test_in_left_empty(self):
        b = Board(8)
        self.assertRaises(EmptyBoardException, b.in_left)

    def test_getitem_Exception(self):
        b = Board(8)
        self.assertEqual(b[3], None)

    def test_contains(self):
        b = Board(8)
        d1 = Domino(2, 3)
        d2 = Domino(4, 4)
        b.add(d1)
        self.assertTrue(d1 in b, False)
        self.assertFalse(d2 in b, True)

    def test_eq_ne(self):
        b1 = Board(8)
        b2 = Board(9)
        self.assertFalse(b1 == b2, True)
        b3 = Board(8)
        d1 = Domino(2, 3)
        d2 = Domino(3, 4)
        d3 = Domino(4, 1)
        d4 = Domino(4, 2)
        b1.add(d1)
        b1.add(d2)
        b3.add(d1)
        b3.add(d2)
        self.assertTrue(b1 == b3, False)
        self.assertFalse(b1 != b3, True)
        b1.add(d3)
        b3.add(d4)
        self.assertFalse(b1 == b3, True)
        self.assertTrue(b1 != b3, False)

