import numpy as np

N = 7

M = 10

L = 3

A = np.random.randint(0, 10, (N, M))

print(A)

row = np.random.randint(low=-9, high=10, size=M)

print("Строка для вставки: " + str(row))

A = np.insert(A, L, row, axis=0)

print("Новая матрица:\n" + str(A))