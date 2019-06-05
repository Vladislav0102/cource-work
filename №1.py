import numpy as np

N = 7

M = 10

A = np.random.randint(0, 100, (N, M))

print(A)

sum = A.sum(axis=0)

i = sum.argmax(axis=0)

max = A.max(axis=0)

max = max[i]

print("Наибольшее значение: " + str(max))