def fibo2(n):
	out = []
	for i in range(1,n+1):
		if i <= 2:
			out.append(1)
		else:
			out.append(out[i-3] + out[i-2])
	return out
