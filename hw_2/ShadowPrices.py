import numpy as np

A = np.matrix([[6., 5.], [10., 20.]])
b = np.matrix([[62.], [150.]])

x = np.linalg.solve(A,b)
x1, x2 = x[0], x[1]

zs = 500. * x1 + 450. * x2
zp = 5221. + 3./7.

shallow = zs - zp

print "x1 = " + str(x1)
print "x2 = " + str(x2)
print "zs = " + str(zs)
print "Shallow price = " + str(shallow)
