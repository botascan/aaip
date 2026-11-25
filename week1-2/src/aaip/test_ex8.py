import unittest

from ex8 import calc


class TestAverage(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(calc([1, 2, 3, 4]), 2.5)

    def test_negative_numbers(self):
        self.assertEqual(calc([-1, -2, -3]), -2)
        self.assertEqual(calc([-4, 2]), -1)

    def test_empty_list(self):
        self.assertIsNone(calc([]))

    def test_single_element(self):
        self.assertEqual(calc([7]), 7)


if __name__ == "__main__":
    unittest.main()
