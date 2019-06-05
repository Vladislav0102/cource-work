import numpy as np

N = 7

M = 7

K = 2

A = np.random.randint(0, 10, (N, M))

print(A)

M_n = np.sum(A, axis=0) * (-1)

A = np.vstack((A, M_n))

print("Новая матрица:\n" + str(A))