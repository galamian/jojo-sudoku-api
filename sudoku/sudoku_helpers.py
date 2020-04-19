def string_to_matrix(s, n):
    return [[(parse_int(s[i*n+j]) if i*n+j < len(s) else 0) for j in range(n)] for i in range(n)]

def parse_int(a, default=0):
    try:
        value = int(a)
    except ValueError:
        value = default
    return value