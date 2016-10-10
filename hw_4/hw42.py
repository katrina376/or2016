import pivot as pv
import numpy as np

'''
min z = 2x1 + 3x2 + 4x3
x1 - x2 + x3 >= 10
x1 - 2x2 + 3x3 >= 6
3x1 - 4x2 + 5x3 >= 15
x1, x2, x3 >= 0

max z* = -2x1 - 3x2 -4x3
-x1 + x2 - x3 <= -10
-x1 + 2x2 + 3x3 <= -6
-3x1 + 4x2 - 5x3 <= -15

max -x0 ; max z* = v - 2x1 - 3x2 -4x3
s1 = x0 - 10 + x1 - x2 + x3
s2 = x0 - 6 + x1 - 2x2 + 3x3
s3 = x0 - 15 + 3x1 - 4x2 + 5x3

max x0 = v ; max z* + 2x1 + 3x2 + 4x3 = v
s1 - x0 - x1 + x2 - x3 = -10
s2 - x0 - x1 + 2x2 - 3x3 = -6
s3 - x0 - 3x1 + 4x2 - 5x3 = -15
'''

# PHASE 1
#      z*, x0, x1, x2, x3, s1, s2, s3,  b
A = [[  0,  1,  0,  0,  0,  0,  0,  0,  0],
     [  1,  0,  2,  3,  4,  0,  0,  0,  0],
	 [  0, -1, -1,  1, -1,  1,  0,  0,-10],
	 [  0, -1, -1,  2, -3,  0,  1,  0, -6],
	 [  0, -1, -3,  4, -5,  0,  0,  1,-15]]

BV = [1, 5, 6, 7]

# Pivot x0 into s3 (3rd constraint)
[A,BV] = pv.pivot(A,BV,4,1)
print A

# Pivot x3 into s1 (1st constraint)
[A,BV] = pv.pivot(A,BV,2,4)
print A

# Pivot x1 into x3 (1st constraint)
[A,BV] = pv.pivot(A,BV,2,2)
print A

# Pivot x2 into s2 (2nd constraint)
[A,BV] = pv.pivot(A,BV,3,3)
print A

# Pivot s3 into x0 (3nd constraint)
[A,BV] = pv.pivot(A,BV,4,7)
print A

# PHASE 2
# Pivot s2 into x2 (2nd constraint)
[A,BV] = pv.pivot(A,BV,3,6)
print A
