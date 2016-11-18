# calculate the power mod.
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
