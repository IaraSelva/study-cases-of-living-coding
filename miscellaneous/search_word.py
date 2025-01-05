class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

    def __repr__(self) -> str:
        return f"children = {self.children}, is_end = {self.is_end}"

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def __repr__(self) -> str:
        return f"{self.root}"
    
    def insert(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True 


class Board:
    def __init__(self, board, words) -> None:
        self.board = board
        self.words = words
        self.trie = self.insert_words()
        self.response = set()

    def search_words(self):
        return self.get_path_board()
    
    def insert_words(self):
        new_trie = Trie()
        for word in self.words:
            new_trie.insert(word)
        return new_trie
    
    def find_word(self, row, col, visited, curr, word):
        row_inbound = row >= 0 and row < len(self.board)
        col_inbound = col >= 0 and col < len(self.board[0])
        if not row_inbound or not col_inbound: return

        position = (row,col)
        if position in visited: return
        visited.add((row, col))

        char = self.board[row][col]
        if char not in curr.children: return
        
        curr = curr.children[self.board[row][col]]
        word += char

        if curr.is_end: return word
        
        return self.find_word(row+1, col, visited, curr, word) or \
        self.find_word(row-1, col, visited, curr, word) or \
        self.find_word(row, col+1, visited, curr, word) or \
        self.find_word(row, col-1, visited, curr, word)
        
        visited.remove((row,col))
        
    
    def get_path_board(self):
        curr = self.trie.root
        word = ''

        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                res = self.find_word(row, col, set(), curr, word)
                if res:
                    self.response.add(res)

        return list(self.response)



board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

start = Board(board, words)

print(start.search_words())
    





        