def blur_image(matrix, radius):
    new_matrix = []
    
    for row in range(len(matrix)):
        new_row = []
        for col in range(len(matrix[0])):
            neighbors = find_neighbors(matrix, row, col, radius)
            print(f"row - col = {row}-{col}")
            print(f"neighbors = {neighbors}")
            new_row.append(sum(neighbors)/len(neighbors))
            print(new_matrix)
            print("\n")
        new_matrix.append(new_row)

    return new_matrix

def find_neighbors(matrix, row, col, radius):
    neighbors = []
    range_row = range(max(0,row-radius), min(row+radius+1, len(matrix)))
    range_col = range(max(0, col-radius), min(col+radius+1, len(matrix[0])))

    for r in range_row:
        for c in range_col:
            neighbors.append(matrix[r][c])
    
    return neighbors

matrix = [[0,1,2,3,0],
          [1,2,4,0,2],
          [1,2,0,1,1]]
radius = 1
print(blur_image(matrix, radius))
