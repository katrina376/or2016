import numpy as np

def pivot(A, BV, r, c) :
	A = np.array(A)
	A = A.astype(float)
	A[r,:] = A[r,:] / A[r,c]
	rows = len(A)
	for i in range(rows) :
		if i != r:
			A[i,:] = A[i,:] - A[i,c] * A[r,:]
	BV[r-1] = c
	return A, BV
