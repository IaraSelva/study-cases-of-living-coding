def count_islands(board):
    count = 0
    visited = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if search_islands(board, row, col, visited):
                count += 1
    
    return count

def search_islands(board, row, col, visited):
    row_inbound = row >= 0 and row < len(board)
    col_inbound = col >= 0 and col < len(board[0])
    if not row_inbound or not col_inbound: return False

    coords = (row, col)
    if coords in visited: return False

    visited.add(coords)
    if board[row][col] == "0": return False 

    search_islands(board, row+1, col, visited)
    search_islands(board, row-1, col, visited)
    search_islands(board, row, col+1, visited)
    search_islands(board, row, col-1, visited)
    return True

print(count_islands([["1"],["1"]]))