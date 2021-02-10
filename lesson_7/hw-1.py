class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for row in self.matrix:
            result += f'{" ".join(map(str, row))}\n'
        return result

    def __add__(self, other):

        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) != len(other.matrix[i]):
                    raise ValueError('Массивы разной длины')
            else:
                return Matrix([[first_matrix[i] + second_matrix[i] for i in range(len(first_matrix))]
                               for first_matrix, second_matrix in zip(self.matrix, other.matrix)])
        else:
            raise ValueError('Массивы разной длины')


matrix_1 = Matrix([[10, 20], [30, 40]])
matrix_2 = Matrix([[1, 2], [3, 4]])
matrix_3 = matrix_1 + matrix_2

print(matrix_3)

