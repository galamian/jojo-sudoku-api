import numpy as np
import time


class SudokuExactCoverGenerator:

    def __init__(self, base=3):
        self.base = base

    @property
    def m(self):
        return self.base * self.base

    @property
    def n(self):
        return self.m * self.m

    def generate(self):
        start = time.time()
        a = np.array([
            [self.exact_cover_map(i + 1, j + 1)
             for j in range(4 * self.m * self.m)]
            for i in range(self.m * self.m * self.m)])
        # print('time elapsed:', time.time()-start, 'seconds')
        return a

    def exact_cover_map(self, row, col):
        i_r, j_r, k_r = self.row_index_map(row)
        f_c, u_c, v_c = self.col_index_map(col)
        return 1 if f_c(i_r, j_r, k_r, u_c, v_c) else 0

    def row_index_map(self, row):
        x, y, z = np.unravel_index(row-1, (self.m, self.m, self.m), order='F')
        return x+1, y+1, z+1
        # return (row - 1) % self.m + 1, (-(- row // self.m) - 1) % self.m + 1, - (- row // self.n )

    def col_index_map(self, col):
        if col < 1:
            raise ValueError
        elif col <= self.n:
            col_c = col

            # 1st constraint: one digit per cell
            def f_c(i, j, k, u, v):
                return i == u and j == v
        elif col <= 2 * self.n:
            col_c = col - self.n

            # 2nd constraint: each digit once per row
            def f_c(i, j, k, u, v):
                return i == u and k == v
        elif col <= 3 * self.n:
            col_c = col - 2 * self.n

            # 3rd constraint: each digit once per column
            def f_c(i, j, k, u, v):
                return j == u and k == v
        elif col <= 4 * self.n:
            col_c = col - 3 * self.n

            # 4th constraint: each digit once per block
            def f_c(i, j, k, u, v):
                return self.block_index_map(i, j) == u and k == v
        else:
            raise ValueError

        ret1, ret2 = np.unravel_index(col_c-1, (self.m, self.m), order='F')
        return f_c, ret1+1, ret2+1
        # return f_c, (col_c - 1) % self.m + 1, (col_c - 1) // self.m + 1

    def block_index_map(self, i, j):
        return self.base * ((i-1) // self.base) + ((j-1) // self.base) + 1
