import numpy as np

N = 7

M = 7

K = 2

A = np.random.randint(0, 10, (N, M))

print(A)

A = np.random.randint(low=-9, high=10, size=(N, M))

print("Матрица:\r\n{}\n".format(A))

print("K = " + str(K))

A = np.delete(A, (K-1), axis=1)

print("Новая матрица:\n" + str(A))