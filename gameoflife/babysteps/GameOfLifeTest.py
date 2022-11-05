import unittest

from gameoflife.babysteps.GameOfLife import countActiveNeighbours


class MyTestCase(unittest.TestCase):
    def test_neighbours(self):
        field = [
            [False, False, False],
            [False, True, False],
            [False, False, True],
        ]
        self.assertEqual(countActiveNeighbours(field), 1)


if __name__ == '__main__':
    unittest.main()
