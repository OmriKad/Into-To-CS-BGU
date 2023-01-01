from unittest import TestCase
from Collection import Collection


class TestCollection(TestCase):
    def test_get_collection(self):
        col = Collection([1, 2, 3])
        self.assertEqual(col.get_collection(), [1, 2, 3])

    def test_add(self):
        col = Collection([1, 2, 3])
        self.assertRaises(NotImplementedError, col.add, 2, 3)

    def test_getitem(self):
        col = Collection([1, 2, 3])
        self.assertEqual(col.__getitem__(1), 2)
        self.assertEqual(col.__getitem__(4), None)

    def test_eq(self):
        col = Collection([1, 2, 3])
        col2 = Collection([1, 2, 3])
        col3 = Collection([1, 4, 3])
        col4 = Collection(['I', 'Domino', None, 1])
        col5 = Collection(['I', 'Domino', None, 1])
        self.assertEqual(col.__eq__(col2), True)
        self.assertEqual(col.__eq__(col3), False)
        self.assertEqual(col4.__eq__(col5), True)

    def test_ne(self):
        col = Collection([1, 2, 3])
        col2 = Collection([1, 2, 3])
        col3 = Collection([1, 4, 3])
        self.assertEqual(col.__ne__(col2), False)
        self.assertEqual(col.__ne__(col3), True)

    def test_len(self):
        col = Collection([1, 2, 3])
        self.assertEqual(col.__len__(), 3)

    def test_contains(self):
        col = Collection([1, 2, 3])
        col2 = Collection([2, 3, 4])
        self.assertEqual(col2 in col, False)

    def test_str(self):
        col4 = Collection(['I', 'Domino', None, 1])
        self.assertEqual(str(col4), 'IDominoNone1')

    def test_repr(self):
        col4 = Collection(['I', 'Domino', None, 1])
        self.assertEqual(repr(col4), 'IDominoNone1')






