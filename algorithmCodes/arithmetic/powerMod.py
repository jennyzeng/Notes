"""
PowerMod
from cs161 ntoe 12

exponentiation
1. comuting x^y (or in Python notation: x**y)
cannot be a polynomial time operation.
Why?
- answer is too big
- it has ylog_2 (x) bits, so just writing it down takes more than polynomial time
 
 2. instead: using powermod
 

RSA public key system
1. yolu chose big random prime numbers p and q
	* notice that we can check if they are prime in polynomial times
2. choose random number e
3. public e and p*q, keep secret p,q
4. calculate d=1/e mod((p-1)(q-1)), so that:
	if encrypt(m): return m^e mod(p*q)
	if decrypt(m): return m^d mod(p*q)
5. works for any message m that can be encoded as a
	binary number 0<= m <= p*q
"""


# m^e mod n

def pMod(m, e, n):
	if e == 0: return 1
	if e == 1: return m % n
	a = pMod(m, e // 2, n)
	
	if (e % 2 == 0):
		return (a * a) % n
	else:
		return (a * a * m) % n


e = 5
# p = 17, q = 19, n = 17*19
n = 17 * 19

# calculate the power mod when m is in range 10 to 29
for m in range(10, 21):
	print("m = ", m, " c = ", pMod(m, e, n))
