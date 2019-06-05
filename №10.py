import numpy as np

N = 7

M = 10

K = 3

A = np.random.randint(-1, 2, (N, M))

print(A)

K_arr = np.array(A[:, K-1])

K_arr = K_arr[: , np.newaxis]

print("K-ый столбец: \r\n{}\n".format(K_arr))

A = A * K_arr

print("Новая матрица:\n" + str(A))