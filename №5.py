import numpy as np

N = 7

M = 10

A = np.random.randint(0, 100, (N, M))

print(A)

Average_line = A.mean(axis=1)

Average_column = A.mean(axis=0)

Average_line = Average_line[: , np.newaxis]

A = np.hstack((A, Average_line))

Average_column = np.hstack((Average_column, [0.]))

A = np.vstack((A, Average_column))

print("Новая матрица:\n" + str(A))