import numpy as np

N = 7

M = 10


A = np.random.randint(0, 10, (N, M))

print(A)

a = b = np.fliplr(A).diagonal(1)

a_prod = a.prod()

print("Элементы которые выше побочной диагонали: \n" + str(a) + "\nИх сумма = " + str(a_prod))

b = np.fliplr(A).diagonal(-1)

b_prod = b.prod()

print("Элементы которые ниже побочной диагонали: \n" + str(b) + "\nИх сумма = " + str(b_prod))