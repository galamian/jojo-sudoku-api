from sudoku import *
from sudoku_helpers import *

def test_box_side_length():
    inp = [[1]]
    assert box_side_length(inp) == 1
    inp = [[1] * 4] * 4
    assert box_side_length(inp) == 2
    inp = [[0] * 9] * 9
    assert box_side_length(inp) == 3

def test_sudoku_9x9():
    tests = [
                { 
                    "input"  : "530070000600195000098000060800060003400803001700020006060000280000419005000080079",
                    "output" : "534678912672195348198342567859761423426853791713924856961537284287419635345286179",
                    "size": 9
                },
                { 
                    "input"  : "000546009020000007003900004905000070700000020000093000056008000010039000000000806", 
                    "output" : "178546239429381567563927184935214678741865923682793415256478391814639752397152846", 
                    "size": 9
                },
                { 
                    "input"  : "1", 
                    "output" : "123456789456789123789123456214365897365897214897214365531642978642978531978531642", 
                    "size": 9
                },
                { 
                    "input"  : "900080001000406000005070300060000040401060508090000020007030200000705000100040007", 
                    "output" : "926583471713426985845971362362857149471269538598314726657138294284795613139642857", 
                    "size": 9
                },
                # invalid inputs shall return input
                { 
                    "input"  : "0101", 
                    "output" : "0101", 
                    "size": 9
                }
            ]

    for test in tests:
        assert sudoku(string_to_matrix(test["input"], test["size"])) == string_to_matrix(test["output"], test["size"])
    

def test_sudoku_4x4():
    tests = [
                { 
                    "input"  : "0000002342303000", 
                    "output" : "2314142342313142", 
                    "size": 4
                },
                { 
                    "input"  : "4", 
                    "output" : "4123231414323241", 
                    "size": 4
                },
                # invalid inputs shall return input
                { 
                    "input"  : "11", 
                    "output" : "11", 
                    "size": 4
                }
            ]

    for test in tests:
        assert sudoku(string_to_matrix(test["input"], test["size"])) == string_to_matrix(test["output"], test["size"])

