import numpy as np

N = 7

M = 10

A = np.random.randint(0, 100, (N, M))

print(A)

Average = A.mean(axis=1)

i = Average.argmin(axis=0)

min = Average.min(axis=0)

print("Наименьшее среднее значение: " + str(min))