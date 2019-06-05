import numpy as np

N = 7

M = 7

A = np.random.randint(0, 10, (N, M))

print(A)

B = (A + A.T)/2

print("Новая матрица:\n" + str(A))