import numpy as np

N = 7

M = 10

H = 4

A = np.random.randint(0, 10, (N, M))

print(A)

bool = A == H

col_sum = np.sum(bool, axis=1)

print("Строки в которых встречается значение: " + str(H))

print(np.argwhere(col_sum).flatten())

print("Строки в которых нет значения: " + str(H))

print(np.argwhere(col_sum == 0).flatten())