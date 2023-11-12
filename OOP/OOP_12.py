import random


class Matrix:
    def __init__(self, rows, columns, matrix=None):
        self.rows = rows
        self.columns = columns
        self.matrix = [[random.randint(1, 10) for _ in range(rows)] for _ in range(columns)] if matrix is None else matrix

    def __str__(self):
        return f'{self.matrix}'

    def __add__(self, other):
        new_matrix = []
        new_matrix_row = []
        for i in range(self.columns):
            for j in range(self.rows):
                new_matrix_row.append(self.matrix[i][j] + other.matrix[i][j])
            new_matrix.append(new_matrix_row)
        return new_matrix

