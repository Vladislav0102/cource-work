import numpy as np

N = 7

M = 10

L = 4

K = 2

A = np.random.randint(0, 10, (N, M))

print(A)

A = np.random.randint(low=-9, high=10, size=(N, M))

print("Матрица:\r\n{}\n".format(A))

x = A[0:L ,0:K]

x_sum = x.sum()

print("Вверхняя левая часть: сумма равна = " + str(x_sum) + "\n" + str(x))

y = A[L: ,0 :K]

y_sum = y.sum()

print("\nНижняя левая часть: сумма равна = " + str(y_sum) + "\n" + str(y))

z = A[0:L ,K:]

z_sum = z.sum()

print("\nВверхняя правая часть: сумма равна = " + str(z_sum) + "\n" + str(z))

a = A[L: ,K:]

a_sum = a.sum()

print("\nНижняя правая часть: сумма равна = " + str(a_sum) + "\n" + str(a))