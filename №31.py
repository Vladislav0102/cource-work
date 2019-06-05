import numpy as np

N = 7

M = 7

K = 2

A = np.random.randint(0, 10, (N, M))

print(A)

M_n = np.sum(A, axis=1) * (-1)

A = np.hstack((A, M_n.reshape(-1, 1)))

print("Новая матрица:\n" + str(A))