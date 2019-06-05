import numpy as np

N = 7

M = 10

L = 3

A = np.random.randint(0, 10, (N, M))

print(A)

A = np.delete(A, (L-1), axis=0)

print("Новая матрица:\n" + str(A))