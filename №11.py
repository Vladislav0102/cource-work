import numpy as np

N = 7

M = 10

L = 3

A = np.random.randint(-1, 2, (N, M))

print(A)

L_arr = np.array(A[L-1, :])

print("L страка: \r\n{}\n".format(L_arr))

A = A + L_arr

print("Новая матрица:\n" + str(A))