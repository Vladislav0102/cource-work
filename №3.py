import numpy as np

N = 7

M = 10

A = np.random.randint(0, 100, (N, M))

print(A)

sum = A.sum(axis=0)

i = sum.argmin(axis=0)

min = A.min(axis=0)

min = min[i]

print("Наименьшее значение: " + str(min))