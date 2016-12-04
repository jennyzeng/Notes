import math
"""
Karatsuba multiplication
cs161 note 12

time analysis:
master theorem (assuming the arithmetic takes O(1))
T(n) = 3T(n/2) + O(n)
a = 3, b = 2, c= 1, d = 0
log_b(a) = log_2(3) > c=1
T(n) = O(n^log_b(a)) = O(n^log_2(3))
O(n) in current level because we have to concatenate p,q,r into n bits
"""

def convertBase(x, base):
	output = ""

	while int(x) >= base:
		output = str(int(x) % base) + output
		x = str(int(x) // base)

	output = str(int(x) % base) + output
	return output


def karatsuba(x, y):
	n = max(len(convertBase(str(x), 2)), len(convertBase(str(y), 2)))
	# base case of recursion
	# use built-in machine arithmetic instructions
	if n == 1:  # should be n <= 32 actually...
		return x * y
	# base for recursive subprobs is 2^(n/2)
	nn = math.floor(n / 2)

	# split x, y into top and bottom sets of n/2 bits
	xh = x >> nn
	xl = x & ((1 << nn) - 1)
	yh = y >> nn
	yl = y & ((1 << nn) - 1)

	# recursive calls on inputs of size n/2
	p = karatsuba(xh, yh)
	q = karatsuba(xl, yl)
	r = karatsuba(xh + xl, yh + yl)

	return (p << (nn + nn)) + ((r - p - q) << nn) + q




print(karatsuba(12, 12))
