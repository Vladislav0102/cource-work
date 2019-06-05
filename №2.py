import numpy as np

N = 7

M = 10

A = np.random.randint(0, 100, (N, M))

print(A)

Average = A.mean(axis=1)

i = Average.argmax(axis=0)

max = Average.max(axis=0)

print("Наибольшее среднее значение: " + str(max))