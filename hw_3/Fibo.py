n = int(input("Please input the term n for the Fibonacci sequence: "))

print "The Fibonacci sequence = "

def fibo(n) : 
	if (n <= 2) : 
		return 1
	else :
		return fibo(n-1) + fibo(n-2)

s = ""

for i in range(1, n+1) :
	s += str(fibo(i)) + " "

print s
