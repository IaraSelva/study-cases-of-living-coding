grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
    

def island_count(grid):
    count = 0
    visited = set()
    islands = {}
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            island_size = checkLands(grid, row, col, visited)
            if island_size > 0:
                count += 1
                islands[count] = island_size
    return islands

def checkLands(grid, row, col, visited, island_size = 0):  
  rowBoundaries = 0 <= row and row < len(grid)
  colBoundaries = 0 <= col and col < len(grid[0])
  if(not rowBoundaries or not colBoundaries): return island_size

  relativePosition = str(row) + "," + str(col)
  if relativePosition in visited: return island_size
  visited.add(relativePosition)
  if grid[row][col] == 'W': return island_size

  island_size += 1

  island_size = checkLands(grid, row - 1, col, visited, island_size)
  island_size = checkLands(grid, row + 1, col, visited, island_size)
  island_size = checkLands(grid, row, col - 1, visited, island_size)
  island_size = checkLands(grid, row, col + 1, visited, island_size)
  return island_size
  
print(island_count(grid))
