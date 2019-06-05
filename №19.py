import numpy as np

N = 7

M = 10


A = np.random.randint(0, 10, (N, M))

print(A)

a = np.diagonal(A, 1)

a_sum = a.sum()

print("Элементы которые выше главной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_sum))

b = np.diagonal(A, -1)

b_sum = b.sum()

print("Элементы которые ниже главной диагонали: \n" + str(b) + "\nИх сумма = " + str(a_sum))