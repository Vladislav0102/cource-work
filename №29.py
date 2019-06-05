import numpy as np

N = 7

M = 7

H = 2

A = np.random.randint(0, 10, (N, M))

print(A)

bool = A == H

col_sum = np.sum(bool, axis=1)

print("Строки в которых встречается значение {}:".format(H))

print(np.argwhere(col_sum).flatten())

print("Строки в которых нет значения {}:".format(H))

print(np.argwhere(col_sum == 0).flatten())