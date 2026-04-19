class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self, size):
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append(0)
            self.board.append(row)
    
    def print_board(self):
        for row in self.board:
            for element in row:
                print(f"| {element} ", end="")
            print("|")


    def make_a_movement(self, position=tuple):
        print(f"making a movement... starting at: {position}")
        limit_row = position[0] >= 0 and position[0] < len(self.board)
        limit_col = position[1] >= 0 and position[1] < len(self.board[0])

        if not limit_row or not limit_col:
            print("board limits traspassed")
            return
        if self.board[position[0]][position[1]] != 0:
            print("place already taken")
            return
        
        self.board[position[0]][position[1]] = "X"
        print("movement has been made")
        self.print_board()

        message = "You won"
        if position[0] == position[1] or position[1] == len(self.board)-1-position[0]:
            if self.check_diagonal() or self.check_reversed_diagonal(): 
                print(message) 
                return
        if self.check_horizontal(position[0]) or self.check_vertical(position[1]): 
            print(message)
            return

        print("keep trying")


    def check_horizontal(self, initial_row):
        for i in range(len(self.board[0])):
            if self.board[initial_row][i] != "X":
                return False
        return True
    
    def check_vertical(self, initial_col):
        for i in range(len(self.board)):
            if self.board[i][initial_col] != "X":
                return False
        return True
        
    def check_diagonal(self):
        for i in range(len(self.board)):
            if self.board[i][i] != "X":
                return False
        return True
    
    def check_reversed_diagonal(self):
        for i in range(len(self.board)):
            if self.board[i][len(self.board)-1-i] != "X":
                return False
        return True
    

game = TicTacToe()
game.create_board(3)
game.print_board()
#game.make_a_movement((1,1))
#game.make_a_movement((1,1))
#game.make_a_movement((0,2))
#game.make_a_movement((2,0))
game.make_a_movement((3,0))


