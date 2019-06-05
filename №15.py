import numpy as np

N = 7

M = 10

H = 4

A = np.random.randint(0, 10, (N, M))

print(A)

a = []

b = []

for i in range(M):
    if H in A[:, i]:
        a.append(i+1)
    else:
        b.append(i+1)

print("Столбцы, которые имеют хотя бы одно число H - {}\n".format(a))

print("Столбцы, которые не имеют это число - {}\n".format(b))