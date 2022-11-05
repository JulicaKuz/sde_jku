import unittest

from gameoflife.babysteps.GameOfLife import countActiveNeighbours, generate_next_round


class MyTestCase(unittest.TestCase):
    def test_neighbours(self):
        field = [
            [False, False, False],
            [False, True, False],
            [False, False, True],
        ]
        self.assertEqual(countActiveNeighbours(field), 1)

    def test_neighbours2(self):
        field = [
            [False, False, False],
            [True, True, False],
            [False, True, True],
        ]
        self.assertEqual(countActiveNeighbours(field), 3)

    def test_neighbours3(self):
        field = [
            [False, False, False],
            [True, False, False],
            [False, True, True],
        ]
        self.assertEqual(countActiveNeighbours(field), 3)

    def test_reproduction(self):
        field = [
            [False, False, False],
            [True, False, False],
            [False, True, True],
        ]

        self.assertTrue(generate_next_round(field))

    def test_underpopulation(self):
        field = [
            [False, False, False],
            [False, True, False],
            [False, False, True],
        ]

        self.assertFalse(generate_next_round(field))
    def test_overcrowding(self):
        field = [
            [True, True, True],
            [True, True, True],
            [True, True, True],
        ]

        self.assertFalse(generate_next_round(field))


if __name__ == '__main__':
    unittest.main()
