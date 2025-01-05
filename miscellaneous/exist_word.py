class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word

        for row in range(len(board)):
            for col in range(len(board[0])):
                  if self.isFirst(row, col) and self.findNewPath(row, col, set()):
                    return True
        return False

    def isFirst(self, row, col):
        return self.board[row][col] == self.word[0]
    
    def findNewPath(self, row, col, visited, index_char = 0):
        print(f"row: {row}")
        print(f"col: {col}")
        print(f"index: {index_char}")
        print(f"char_index {self.word[index_char]}")
        print(f"visited: {visited}")
        print("------------------------------------------------------")

        rowInbound = 0 <= row and row < len(self.board)
        colInbound = 0 <= col and col < len(self.board[0])
        if not rowInbound or not colInbound: return False

        position = str(row) + "," + str(col)
        if position in visited: return False

        if self.word[index_char] != self.board[row][col]:
            return False
        if index_char == len(self.word) - 1:
            return True
        
        visited.add(position)
        index_char += 1
        return self.findNewPath(row + 1, col, visited, index_char) or \
        self.findNewPath(row - 1, col, visited, index_char) or \
        self.findNewPath(row, col + 1, visited, index_char) or \
        self.findNewPath(row, col - 1, visited, index_char)
    

solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
[["A","B","C","E"],
 ["S","F","E","S"],
 ["A","D","E","E"]]

    