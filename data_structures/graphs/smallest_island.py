grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

def minimum_island(grid):
  min_size = len(grid) * len(grid[0])
  visited = set()
  for row in (range(len(grid))):
    for col in (range(len(grid[0]))):
      size = findSmallest(grid, row, col, visited)
      if size > 0 and size < min_size: 
        min_size = size
  return min_size

def findSmallest(grid, row, col, visited, size = 0):
  rowBoundary = 0 <= row and row < len(grid)
  colBoundary = 0 <= col and col < len(grid[0])
  if not rowBoundary or not colBoundary: return size
  
  position = str(row)+","+str(col)
  if position in visited: return size
  visited.add(position)
  
  if grid[row][col] == 'W': return size

  size += 1
  
  size = findSmallest(grid, row -1, col, visited, size)
  size = findSmallest(grid, row +1, col, visited, size)
  size = findSmallest(grid, row, col -1, visited, size)
  size = findSmallest(grid, row, col +1, visited, size)
  return size

print(minimum_island(grid))
