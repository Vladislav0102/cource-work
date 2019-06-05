import numpy as np

N = 7

M = 10

L = 2

K = 3

A = np.random.randint(-1, 2, (N, M))

print(A)

Ln = 0

Kn = 0

for i in A[:L].flat:
    if i == 0:
        Ln += 1

for i in A[:, : K].flat:
    if i == 0:
        Kn += 1

print("Количество нулевых элементов в верхних " + str(L) + " строках матрицы - " + str(Ln))

print("Количество нулевых элементов в левых " + str(K) + " столбцах матрицы - " + str(Kn))