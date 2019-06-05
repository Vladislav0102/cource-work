import numpy as np

N = 7

M = 10

A = np.random.randint(-1, 2, (N, M))

print(A)

Max = A.max(axis=1)

Max = np.array(Max)[: , np.newaxis]

A = A / Max

print("Новая матрица:\n" + str(A))