class matrix:
    def __init__(self):
        self.matrix = []
    
    def create_matrix(self, n_of_row, n_of_col):
        for i in range(n_of_row):
            row = []
            for j in range(n_of_col):
                row.append((i,j))
            self.matrix.append(row)

    def print_matrix(self):
        for row in self.matrix:
            for e in row:
                print(e, end = " ")
            print(" ")

    def create_personalized_matrix(self):
        n_of_rows = int(input("digite a quantidade de linhas: "))
        n_of_col = int(input("digite a quantidade de colunas: "))
        for _ in range(n_of_rows):
            row = []
            for _ in range(n_of_col):
                element = input("digite um elemento: ")
                row.append(element)
            self.matrix.append(row)
        self.print_personalized_matriz()

    def print_personalized_matriz(self):
        for row in self.matrix:
            for element in row:
                print(f"| {element} ", end="")
            print("|")

    def sum_n_to_matrix(self):
        n = input("qual número será somado aos elementos da matriz? ")
        for row in self.matrix:
            for i, element in enumerate(row):
                row[i] = int(element) + int(n)  
        self.print_personalized_matriz()

    def compare_matrices_size(self, other):
        if type(other) == matrix:
            if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                return False
            return True
        print("tipo errado. aceitamos apenas matrizes")
        return False
    
    def compare_matrices(self, other):
        if self.compare_matrices_size(other):
            for i, row in enumerate(self.matrix):
                for j, element in enumerate(row):
                    if element != other.matrix[i][j]:
                        return False
            return True
        return False

    def is_identity_matrix(self):
        if len(self.matrix) == len(self.matrix[0]):
            for i, row in enumerate(self.matrix):
                for j, element in enumerate(row):
                    if (i == j and int(element) != 1) or (i != j and int(element) != 0):
                        return False
            return True
        return False
    
    def create_identity_matrix(self):
        size = int(input("digite o tamanho da matriz identidade: "))
        for i in range(size):
            row = []
            for j in range(size):
                if i == j:
                    row.append(1)
                else: row.append(0)
            self.matrix.append(row)
        self.print_personalized_matriz()

    
    def tranpose_matrix(self):
        n_of_rows = len(self.matrix)
        n_of_cols = len(self.matrix[0])

        transposed_matrix = [[0] * n_of_rows for _ in range(n_of_cols)]

        for i, row in enumerate(self.matrix):
            for j, element in enumerate(row):
                transposed_matrix[j][i] = element

        tm = matrix()
        tm.matrix = transposed_matrix
        return tm
    


minha_matriz = matrix()
minha_matriz.create_matrix(3,4)
#minha_matriz.print_matrix()

#minha_matriz.create_personalized_matrix()

#minha_matriz_2 = matrix()
#minha_matriz_2.create_personalized_matrix()
#minha_matriz_2.sum_n_to_matrix()

#print(minha_matriz.compare_matrices_size(minha_matriz_2))

#print(minha_matriz.compare_matrices(minha_matriz_2))

#print(minha_matriz.is_identity_matrix())

#minha_matriz.create_identity_matrix()

tm = minha_matriz.tranpose_matrix()
tm.print_personalized_matriz()



