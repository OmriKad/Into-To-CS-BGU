from unittest import TestCase
from Domino import Domino
from Hand import Hand
from Collection import Collection
from Exceptions import NoSuchDominoException


class TestHand(TestCase):
    def test_add(self):
        d1 = Domino(2, 3)
        d2 = Domino(3, 6)
        d3 = Domino(6, 6)
        hand1 = Hand([d1])
        self.assertEqual(str(hand1), '[2|3]')
        hand1.add(d2)
        self.assertEqual(str(hand1), '[2|3][3|6]')
        hand1.add(d3, 1)
        self.assertEqual(str(hand1), '[2|3][6|6][3|6]')

    def test_remove_domino(self):
        d1 = Domino(2, 3)
        d2 = Domino(3, 6)
        d3 = Domino(6, 6)
        hand1 = Hand([d1])
        hand1.add(d2)
        hand1.add(d3, 1)
        hand1.remove_domino(d3)
        self.assertEqual(str(hand1), '[2|3][3|6]')
        hand1.remove_domino(d2)
        self.assertEqual(str(hand1), '[2|3]')

    def test_getitem_contains_eq_ne_len(self):
        d1 = Domino(2, 3)
        d2 = Domino(3, 6)
        d3 = Domino(6, 6)
        d4 = Domino(1, 6)
        hand1 = Hand([d1])
        hand1.add(d2)
        hand1.add(d3)
        hand2 = Hand([d1])
        hand2.add(d2)
        hand2.add(d3)
        self.assertEqual(len(hand1), 3)
        self.assertEqual(hand1[1], d2)
        self.assertEqual(hand1[4], None)
        self.assertTrue(d2 in hand1, False)
        self.assertFalse(d4 in hand1, True)
        self.assertTrue(hand1 == hand2, False)
        self.assertFalse(hand1 != hand2, True)
        hand1.add(d4)
        self.assertFalse(hand1 == hand2, True)
        self.assertTrue(hand1 != hand2, False)


