import numpy as np

N = 7

M = 10

A = np.random.randint(0, 100, (N, M))

print(A)

Sum = A.sum()

print("Сумма элементов всей матрицы: " + str(Sum) + "\n")

Sum_column = A.sum(axis=1)

X = []

for i in range(0, N):
    n = Sum_column[i] / Sum
    X.append(n)

X = np.array(X)[: , np.newaxis]

A = np.hstack((A, X))

print("Новая матрица:\n" + str(A))