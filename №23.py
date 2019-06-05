import numpy as np

N = 7

M = 10

A = np.random.randint(0, 10, (N, M))

print(A)

iu = np.triu_indices(N, 1)

a = A[iu]

a = np.sum(np.array(a))

print("\nCумма элементов выше главной диагонали = " + str(a))

b = np.fliplr(A)[iu]

b = np.prod(np.array(b))

print("\nПроизведение элементов выше побочной диагонали = " + str(b))