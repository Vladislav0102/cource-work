import numpy
def FancyPrint(A, B, selected):
    for row in range(len(B)):
        print("(", end='')
        for col in range(len(A[row])):
            print("\t{1:10.2f}{0}".format(" " if (selected is None or selected != (row, col)) else "*", A[row][col]), end='')
            print("\t) * (\tX{0}) = (\t{1:10.2f})".format(row + 1, B[row]))

data = numpy.genfromtxt('./Gauss.csv', delimiter=';')
m_list = []
m = []
for row in data:
    first_col = row[0]
    if numpy.isnan(first_col):
        m_list.append(m)
        m = []
        continue

    mask = ~numpy.isnan(row)
    m.append(row[mask])
m_list.append(m)

f = open('numpy-gauss-slv.csv', 'wb+')
f.truncate()
for m in m_list:
    M = numpy.array(m)
    myA = numpy.delete(M, M.shape[1] - 1, axis=1)
    myB = M[:, [-1]].flatten()
    slv = numpy.linalg.solve(myA, myB)
    print("Решение:")
    print(slv)
    numpy.savetxt(f, numpy.array([slv]), delimiter=',')
f.close()
