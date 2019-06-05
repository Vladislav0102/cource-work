import numpy as np

N = 7

M = 10

A = np.random.randint(0, 10, (N, M))

print(A)

col = [i % 2 for i in np.sum(A, axis=1)]

A = np.insert(A, M, col, axis=1)

print("Новая матрица:\n" + str(A))