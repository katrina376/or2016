import numpy as np
np.seterr(divide='ignore', invalid='ignore')

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

def find_pivot(A, BV) :
	rows = len(A)
	cols = len(A[0,:])
	pv = -1
	for i in range(cols-1) : 
		if (A[0,i] < 0) :
			pv = i
	for i in range(cols-1) : 
		if (not pv == -1) and (A[0,i] < A[0,pv]) :
			pv = i
	return pv

def check_optimal(A,BV) :
	rows = len(A)
	c = find_pivot(A,BV)
	if (c == -1) :
		return [A, BV]
	else :
		R = A[:,rows-1] / A[:,c]
		r = -1
		for i in range(rows) :
			if (R[i] > 0) :
				r = i
		for i in range(rows) :
			if (not r == -1) and (R[i] < R[r]) and (R[i] > 0):
				r = i
		if (r == -1):
			return [A, BV]
		[A, BV] = pivot(A, BV, r, c)
		check_optimal(A,BV)

def simplex_method(A, BV) :
	A = np.array(A)
	A = A.astype(float)
	rows = len(A)
	cols = len(A[0,:])
	# check bijs
	for i in range(1,rows) :
		if A[i,cols-1] < 0 :
			err = [True, "Not feasible in initial state, try other methods."]
			return [err, A, BV]
	# check optimal
	[A, BV] = check_optimal(A, BV)
	print A
	err = [False, "The simplex method is finished."]
	return [err, A, BV]

