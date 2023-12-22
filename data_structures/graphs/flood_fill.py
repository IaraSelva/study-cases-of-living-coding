screen = [[1, 1, 1, 1, 1, 1, 1, 1], 
          [1, 1, 1, 1, 1, 1, 0, 0], 
          [1, 0, 0, 1, 1, 0, 1, 1], 
          [1, 2, 2, 2, 2, 0, 1, 0], 
          [1, 1, 1, 2, 2, 0, 1, 0], 
          [1, 1, 1, 2, 2, 2, 2, 0], 
          [1, 1, 1, 1, 1, 2, 1, 1], 
          [1, 1, 1, 1, 1, 2, 2, 1]]


def floodFill(grid, x, y, newColor):
    presentColor = grid[x][y]
    if presentColor == newColor:
        return
    return replaceColor(grid, x, y, presentColor, newColor)

def replaceColor(grid, x, y, presentColor, newColor, visited = set()):
    rowInbound = 0 <= x and x < len(grid)
    colInbound = 0 <= x and x < len(grid[0])
    if not rowInbound or not colInbound: return

    if grid[x][y] in visited: return
    if not grid[x][y] == presentColor: return

    position = str(x)+","+str(y)
    visited.add(position)
    print(grid[x][y])

    grid[x][y] = newColor
    replaceColor(grid, x + 1, y, presentColor, newColor, visited)
    replaceColor(grid, x - 1, y, presentColor, newColor, visited)
    replaceColor(grid, x, y + 1, presentColor, newColor, visited)
    replaceColor(grid, x, y - 1, presentColor, newColor, visited)
    return grid

print(floodFill(screen, 4, 4, 3))
    