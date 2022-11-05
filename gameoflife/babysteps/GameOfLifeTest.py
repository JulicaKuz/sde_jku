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



if __name__ == '__main__':
    unittest.main()
