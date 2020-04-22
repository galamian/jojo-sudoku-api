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


def string_to_matrix(s, n):
    return [[(parse_int(s[i*n+j]) if i*n+j < len(s) else 0) for j in range(n)] for i in range(n)]

def parse_int(character, default=0):
    try:
        value = int(character)
    except ValueError:
        value = default
    return value



def box_side_length(inp):
    return int(len(inp)**(1/2))
