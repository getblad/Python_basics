class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list

    def __str__(self):
        for list in self.matrix:
            for number in list:
                print(number, end=' ')
            print()
        return ''

    def __add__(self, other):
        return Matrix([[i+n for i, n in zip(a, b)] for a, b in zip(self.matrix, other.matrix)])


matrix = [[1, 2, 3, 5], [1, 2, 3, 4], [1, 2, 2, 7]]
matrix2 = [[1, 2, 3, 5], [1, 2, 3, 4], [1, 2, 2, 7]]
ma = Matrix(matrix)
ma2 = Matrix(matrix2)
c = ma + ma2
print(c)
