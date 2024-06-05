import random

def create_lists(rows,cols):
    new_lists = []
    for _ in range(rows):
        inner_list = [random.randrange(50) for _ in range(cols)]
        new_lists.append(inner_list)
    return new_lists

matrix_1 = create_lists(10,10)
matrix_2 = create_lists(10,10)

print(matrix_1)
print(matrix_2)

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2)):
            row.append(matrix1[i][j]+matrix2[i][j])
        result.append(row)
    return result

matrix_3 = add_matrices(matrix_1, matrix_2)
print(matrix_3)