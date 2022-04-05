grid = [["[]", "[]", "[]", "[]", "[]"],
    ["[]", "[]", "[]", "[]", "[]"],
    ["[]", "[]", "[]", "[]", "[]"],
    ["[]", "[]", "[]", "[]", "[]"],
    ["[]", "[]", "[]", "[]", "[]"]]

""" def genGrid(_x, _char):
    _grid = []
    _row = []
    for i in range(_x):
        print(i)
        _row[i] = _char
    for j in range(_x):
        grid[j] = [_row]
    return _grid

grid2 = genGrid(5,"0") """

def print_kaart():
    print('\n'.join(' '.join(str(x) for x in row) for row in grid))

print_kaart()