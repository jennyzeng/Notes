import numpy as np

"""
from cs 161 lecture 1
three different algorithms for Fibnacci Numbers
Definition:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)  if (n>1)
"""


# Recurrence: formula for a collection of values in terms of ealier values
def fib_recur(n):
	if n < 2:
		return n
	else:
		return fib_recur(n - 1) + fib_recur(n - 2)


print("fib recur: ", [fib_recur(i) for i in range(10)])
"""
Time complexity:
Define T(n) = # calls made by fib(n) including the outer call)
T(0) = T(1)  = 1
T(n) = 1 + T(n-1)+T(n-2) for n < 1)
1: top level call
T(n-1): 1st recursive call
T(n-2): 2nd recursive call

- always >= corresponding Fibonacci Numbers (because of the "1+" in the recurrence)
- grow exponentially: ~= 1.618^n
- so fib_recur(n) starts getting slow for n ~= 35, probably maxes out where n~= 50

T(n) = 2 F(n+1)-1

this is a slow algorithm (time ~1.618^n)
e.g. when n = 60, ~10^13 calls
"""


# quicker algorithm, using dynamic programming
# build table of smaller subprogram values, look them up instead of repeatedly re-computing them
def fib_dp(n):
	dp = [None] * (n + 1)  # Assuming n starts with 0, and allocate (n+1) element array dp
	dp[0] = 0
	if n > 0:
		dp[1] = 1
	if n > 1:
		for i in range(2, n + 1):
			dp[i] = dp[i - 1] + dp[i - 2]
	return dp[n]


print("fib dp: ", [fib_dp(i) for i in range(10)])

"""
constant # operations/lines
# lines = 4+2(n-1) = O(n)
4: outside loop
2(n-1) inside loop
loop runs n-1 times
    constant # ops/iteration
    constant # ops outside loop
==> O(n)

from fib_recur to fib_dp, we improve the algorithm from *exponential* to *linear*
"""

"""
we can still do much better, by using a trick from linear algebra
[[a b] *  [[e f]    =  [[ae + bg   af + bh]
 [c d]]    [g h]]       [ce + dg   cf + dh]]

so
([[1  1]          =     [F[n+1]    F[n]]
 [1  0]])^2             [F[n]      F[n-1]]

it can be proved by induction
"""


def power(matrix, n):
	if n == 0:
		return np.array([[1, 1], [1, 1]])  # return identity matrix
	elif n == 1:
		return matrix
	temp = power(matrix, n // 2)
	temp = np.matmul(temp, temp)
	if n % 2 != 0:  # n is odd
		temp = np.matmul(temp, matrix)
	return temp


def fib_pow(n):
	if n == 0: return 0
	temp = np.array([[1, 1], [1, 0]])
	temp = power(temp, n - 1)
	return temp[0][0]  # return top-left coefficient


print("fib pow: ", [fib_pow(i) for i in range(10)])
# time: O(log n)
