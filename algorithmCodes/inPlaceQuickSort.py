# in place quick sort algorithm.
# Input: array of values
# partition: move values around in same array
# (not copying them into a new data structure)

import random


def quickSort(i, j):
	if j - i + 1 <= 1:
		return
	k = random.randint(i, j)
	L[k], L[i] = L[i], L[k]  # swap, L[i] is pivot
	k = partition(i, j)
	if k - 1 > i:
		quickSort(i, k - 1)
	if k + 1 < j:
		quickSort(k + 1, j)


def partition(i, j):
	s = i + 1
	e = j
	while s <= e:
		while s <= e and L[s] < L[i]:
			s += 1
		while s <= e and L[e] > L[i]:
			e -= 1
		if s > e:
			break
		L[s], L[e] = L[e], L[s]
		s += 1
		e -= 1
	L[i], L[s - 1] = L[s - 1], L[i]
	return s-1

L = [0, 9, 4, 1, 5, 2, 7]
quickSort(0, len(L)-1)
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
