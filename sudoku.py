import copy

def sudoku(input):
    """calculates sudoku solution of given 2d-array as a general sudoku problem"""

    # calculate box/sudoku side length m/n
    m = box_side_length(input)
    n = m**2

    # copy input
    puzzle = copy.deepcopy(input)

    # list of steps for backtracking purpose
    attempts = []

    i = 0
    while i<n:
        j = 0
        while j < n:
            if input[i][j]>0:
                if not isValid(input[i][j], i, j, input, m, n):
                    return input
            elif (puzzle[i][j]==9):
                # clear field
                puzzle[i][j]=0

                if len(attempts)==0:
                    return puzzle
                # go back
                i, j, attempts = goBack(i, j, attempts)
                #print(puzzle)
                continue
            else:
                validFound = False
                for temp in range(puzzle[i][j]+1, n+1):
                    # check temp as candidate here
                    
                    
                    if isValid(temp, i, j, puzzle, m, n):
                        # new attempt
                        puzzle[i][j] = temp
                        #if attempts[-1]!=(i,j):
                        attempts.append((i,j))
                        #print("new attempt: " + str(attempts))
                        validFound = True
                        break
                if not validFound:
                    puzzle[i][j] = 0
                    # go back
                    if len(attempts)==0:
                        return puzzle
                    i, j, attempts = goBack(i, j, attempts)
                    #print(puzzle)
                    continue
            j += 1
        i += 1

    return puzzle

def goBack(i, j, attempts):
    """reset i and j to the latest position and delete current step"""
    (i, j) = attempts[-1]
    del attempts[-1]
    return i, j, attempts

def block(i, j, m):
    return [(x, y) for x in range(m*(i//m),m*(i//m)+m) for y in range(m*(j//m),m*(j//m)+m)]

def blockIndex(i, j, m):
    return (i//m)*m + j//m

def isValid(temp, i, j, puzzle, m, n):
    """iterate row/col/block and check sudoku rule for given integer at given position""" 
    valid = True
    b = block(i, j, m)
    for k in range(n):
        if ((k!=j and puzzle[i][k]==temp)
            or
            (k!=i and puzzle[k][j]==temp)
            or
            ((b[k][0],b[k][1])!=(i,j) and puzzle[b[k][0]][b[k][1]]==temp)):
                valid = False
                break
    return valid


def box_side_length(inp):
    return int(len(inp)**(1/2))



