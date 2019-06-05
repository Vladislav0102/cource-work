import numpy as np

N = 7

M = 7

A = np.random.randint(0, 10, (N, M))

print(A)

bool = A == 0

col = np.sum(bool, axis=1)

A = np.insert(A, M, col, axis=1)

row = np.append(np.sum(bool, axis=0), 0)

A = np.insert(A, N, row, axis=0)

print("Новая матрица:\n" + str(A))