#      z*, x1, x2, x3, s1, s2, s3,  b
A = [[  1, -5, -4, -3,  0,  0,  0,  0],
	 [  0,  2,  3,  1,  1,  0,  0,  5],
	 [  0,  4,  1,  2,  0,  1,  0, 11],
	 [  0,  3,  4,  2,  0,  0,  1,  8]]

BV = [4,5,6]

import SimplexMethod as sm
[err, A, BV] = sm.simplex_method(A,BV)
print err[1]
print 'A = ' + str(A)
