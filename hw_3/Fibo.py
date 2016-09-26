n = int(input("Please input the term n for the Fibonacci sequence: "))

print "The Fibonacci sequence = "

s = ""

i0 = 0
i1 = 1
i2 = i0 + i1

for i in range(0,n):
	s += str(i2) + " "
	i2 = i0 + i1
	i0 = i1
	i1 = i2
	
print s
