import copy
from sudoku.sudoku_helpers import *


def solve(inp):
    """calculates sudoku solution of given 2d-array as a general sudoku problem"""

    # calculate box/sudoku side length m/n
    m = box_side_length(inp)
    n = m ** 2

    # copy input
    puzzle = copy.deepcopy(inp)

    # list of steps for backtracking purpose
    attempts = []

    i = 0
    while i < n:
        j = 0
        while j < n:
            if inp[i][j] > 0:
                if not isValid(inp[i][j], i, j, inp, m, n):
                    return inp
            elif puzzle[i][j] == 9:
                # clear field
                puzzle[i][j] = 0

                if len(attempts) == 0:
                    return puzzle
                # go back
                i, j, attempts = go_back(i, j, attempts)
                # print(puzzle)
                continue
            else:
                valid_found = False
                for temp in range(puzzle[i][j] + 1, n + 1):
                    # check temp as candidate here

                    if isValid(temp, i, j, puzzle, m, n):
                        # new attempt
                        puzzle[i][j] = temp
                        # if attempts[-1]!=(i,j):
                        attempts.append((i, j))
                        # print("new attempt: " + str(attempts))
                        valid_found = True
                        break
                if not valid_found:
                    puzzle[i][j] = 0
                    # go back
                    if len(attempts) == 0:
                        return puzzle
                    i, j, attempts = go_back(i, j, attempts)
                    # print(puzzle)
                    continue
            j += 1
        i += 1

    return puzzle


def go_back(i, j, attempts):
    """reset i and j to the latest position and delete current step"""
    (i, j) = attempts[-1]
    del attempts[-1]
    return i, j, attempts
