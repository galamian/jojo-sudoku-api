from sudoku.sudoku_helpers import * 

def test_box_side_length():
    inp = [[1]]
    assert box_side_length(inp) == 1
    inp = [[1] * 4] * 4
    assert box_side_length(inp) == 2
    inp = [[0] * 9] * 9
    assert box_side_length(inp) == 3



