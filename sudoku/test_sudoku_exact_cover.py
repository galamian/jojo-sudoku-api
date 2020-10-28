import unittest
from sudoku.sudoku_exact_cover import SudokuExactCoverGenerator


class MapsTestCase(unittest.TestCase):

    generator = SudokuExactCoverGenerator()

    def test_row_index_map(self):
        self.assertEqual(self.generator.row_index_map(1), (1, 1, 1))
        self.assertEqual(self.generator.row_index_map(81), (9, 9, 1))
        self.assertEqual(self.generator.row_index_map(80), (8, 9, 1))
        self.assertEqual(self.generator.row_index_map(82), (1, 1, 2))
        self.assertEqual(self.generator.row_index_map(83), (2, 1, 2))
        self.assertEqual(self.generator.row_index_map(84), (3, 1, 2))
        self.assertEqual(self.generator.row_index_map(729), (9, 9, 9))

        for x, y, z in zip([5, 4, 8, 7, 9, 1, 9], [1, 2, 2, 3, 3, 3, 9], [1, 2, 3, 5, 7, 8, 2]):
            t = x + 9 * (y - 1) + 81 * (z - 1)
            self.assertEqual(self.generator.row_index_map(t), (x, y, z))

    def test_col_index_map(self):
        tc = {1: (1, 1), 2: (2, 1), 17: (8, 2)}

        # test generation of index values u,v
        for key, value in tc.items():
            u, v = self.generator.col_index_map(key)[1], self.generator.col_index_map(key)[2]
            self.assertEqual((u, v), value)

        # test case: first row has to have a 1 in first row / first column
        t = 1
        f, u, v = self.generator.col_index_map(t)
        self.assertEqual((u, v), (1, 1))
        self.assertEqual(f(1, 1, 1, u, v), 1)

    def test_exact_cover_map(self):
        self.assertEqual(self.generator.exact_cover_map(1, 1), 1)
        self.assertEqual(self.generator.exact_cover_map(2, 1), 0)

    def test_block_index_map(self):
        self.assertEqual(self.generator.block_index_map(9, 9), 9)
        self.assertEqual(self.generator.block_index_map(1, 1), 1)
        self.assertEqual(self.generator.block_index_map(1, 4), 2)
        self.assertEqual(self.generator.block_index_map(3, 2), 1)
        self.assertEqual(self.generator.block_index_map(5, 3), 4)
        self.assertEqual(self.generator.block_index_map(5, 5), 5)
        self.assertEqual(self.generator.block_index_map(5, 7), 6)



if __name__ == '__main__':
    unittest.main()
