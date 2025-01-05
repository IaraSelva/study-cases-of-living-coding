def islands_size(board):
    count = 0
    island_size = {}
    visited = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            size = explore_grid(board, row, col, visited)
            if size:
                print(f"size: {size}")
                count += 1
                island_size[count] = size
    return island_size

def explore_grid(board, row, col, visited, size=0):
    row_inbound = row >= 0 and row < len(board)
    col_inbound = col >= 0 and col < len(board[0])
    if not row_inbound or not col_inbound: return 0

    position = (row,col)
    if position in visited: return 0
    
    visited.add(position)

    if board[row][col] == "0": return 0

    size = 1

    size += explore_grid(board, row+1, col, visited, size)
    size += explore_grid(board, row-1, col, visited, size)
    size += explore_grid(board, row, col+1, visited, size)
    size += explore_grid(board, row, col-1, visited, size)
    return size

print(islands_size([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","1"]
]))

