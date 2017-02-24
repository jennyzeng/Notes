import random

"""
quick select:
find the kth smallest element in a list
k is 0 indexing

"""


def quickSelect(X, k):  # no worse than quicksort
	if len(X) <= 1: return X[0]
	pivot = X[random.randint(0, len(X) - 1)]
	L = []  # items < p
	E = []  # items = p
	G = []  # items > p
	for e in X:
		if e < pivot:
			L.append(e)
		elif e > pivot:
			G.append(e)
		else:
			E.append(e)
	if k < len(L):
		return quickSelect(L, k)
	elif k < (len(L) + len(E)):
		return E[0]
	else:
		return quickSelect(G, (k - len(L) - len(E)))


print(quickSelect([5, 4, 3, 2, 1, 0], 3))
# T(n) = 3T(3/4 n) + O(n) = O(n)
