import numpy as np

N = 7

M = 10

A = np.random.randint(0, 100, (N, M))

print(A)

Sum = A.sum()

B=np.sum(A)

M_sum = np.sum(A, axis=0)/np.sum(A)

A = np.vstack((A,M_sum))

print("Новая матрица:\n" + str(A))