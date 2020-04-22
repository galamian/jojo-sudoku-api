from sudoku.sudoku_helpers import *
from sudoku.solve_backtracking1 import solve as solve_back1


class Sudoku:

    def __init__(self, inp="1", n=9):
        self.input = string_to_matrix(inp, n)

    def check(self):
        pass
        
    
    def solve(self):
        return solve_back1(self.input)


