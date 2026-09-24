import unittest

from sequence_utils import ordered_unique


class OrderedUniqueTests(unittest.TestCase):
    def test_repeated_values_keep_first_occurrence_order(self):
        values = [3, 1, 3, 2, 1, 4, 2, 3]
        original = values.copy()
        self.assertEqual(ordered_unique(values), [3, 1, 2, 4])
        self.assertEqual(values, original)

    def test_empty_input(self):
        values = []
        result = ordered_unique(values)
        self.assertEqual(result, [])
        self.assertEqual(values, [])
        self.assertIsNot(result, values)

    def test_already_unique_input(self):
        values = ['z', 'a', 'm']
        original = values.copy()
        result = ordered_unique(values)
        self.assertEqual(result, original)
        self.assertEqual(values, original)
        self.assertIsNot(result, values)

    def test_mixed_hashable_values(self):
        values = [None, ('a', 1), 'x', None, ('a', 1), 7, 'x']
        self.assertEqual(ordered_unique(values), [None, ('a', 1), 'x', 7])

    def test_generator_input(self):
        values = (value for value in [2, 1, 2, 3, 1])
        self.assertEqual(ordered_unique(values), [2, 1, 3])


if __name__ == '__main__':
    unittest.main()
