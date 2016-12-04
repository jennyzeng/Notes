# in place quick sort algorithm.
# Input: array of values
# partition: move values around in same array
# (not copying them into a new data structure)

import random


# i is start and j is stop index
def quickSort(i, j):
	if j - i + 1 <= 1:
		return
	k = random.randint(i, j)
	swap(L, k, i)# swap, L[i] is pivot
	k = partition(i, j)
	quickSort(i, k - 1)
	quickSort(k + 1, j)


def partition(i, j):
	s = i + 1
	e = j
	while s <= e:
		if L[s] <= L[i]:
			s += 1
		elif L[e] >= L[i]:
			e -= 1
		else:
			swap(L, s, e)
			s += 1
			e -= 1
	swap(L, i, s-1)
	return s - 1


def swap(L, i, j):
	L[i], L[j] = L[j], L[i]


L = [0, 9, 4, 1, 5, 2, 7]
quickSort(0, len(L) - 1)
print(L)
L = [1, 1, -2, 2, 3, 4, 1, 2, 5, 0, -1]
quickSort(0, len(L) - 1)
print(L)
L = [9, 8, 7, 6, 4, 3, 2, 1]
quickSort(0, len(L) - 1)
print(L)
L = [7, 5, 2, 1, 5, 2, 3, 9]
quickSort(0, len(L) - 1)
print(L)
L = [1]
quickSort(0, len(L) - 1)
L = []
print(L)
