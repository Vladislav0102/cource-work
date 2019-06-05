import numpy as np

N = 7

M = 10

A = np.random.randint(0, 10, (N, M))

print(A)

Max = A.max(axis=0)

A = A / Max

print("Новая матрица:\n" + str(A))