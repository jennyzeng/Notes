"""
Greatest common divisors(Euclid)
from cs161 note 12

time: O(n * multiply)
worst case: gcd(Fi, Fi+1) where Fi = Fibonacci
"""


def gcd(x, y):
	if x == 0: return y
	if y == 0: return x
	return gcd(y, x % y)


print(gcd(21, 34))
