""" def genGrid(_x, _char):
    _grid = []
    for i in range(_x):
        _row = []
        for j in range(_x):
           _row.append(_char)
        _grid.append(_row)
    return _grid """

def canMoveRight(_grid, _currentPos):
    if(_grid[_currentPos[0]+1][_currentPos[1]] == "0"):
        return True

def printGrid(_grid):
    print('\n'.join(' '.join(str(x) for x in row) for row in _grid))

#############################
grid = [["12","0","1","0","0"],
        ["0","0","1","0","0"],
        ["0","0","1","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","0","24"]]
startX = 0
startY = 0

print(canMoveRight(grid, [startX, startY]))