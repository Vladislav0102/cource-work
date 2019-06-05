import numpy as np

N = 7

M = 10

A = np.random.randint(0, 10, (N, M))

print(A)

a = np.diagonal(A)

a_sum = a.sum()

print("Главная диагональ: \n" + str(a) + "\n Её сумма = " + str(a_sum))

b = np.fliplr(A).diagonal(0)

b_sum = b.sum()

print("Побочная диагональ: \n" + str(b) + "\n Её сумма = " + str(b_sum))