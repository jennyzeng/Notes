# quickSort, randomized comparison sorting. O(nlogn)
import random


def quickSort(L):
	if len(L) <= 1:
		return L
	pivot = L[random.randint(0, len(L) - 1)]
	left = [x for x in L if x < pivot]
	equal = [x for x in L if x == pivot]
	right = [x for x in L if x > pivot]
	return quickSort(left) + equal + quickSort(right)


print(quickSort([0, 9, 4, 1, 5, 2, 7]))
print(quickSort([1, 1, -2, 2, 3, 4, 1, 2, 5, 0, -1]))
print(quickSort([9, 8, 7, 6, 4, 3, 2, 1]))
print(quickSort([7, 5, 2, 1, 5, 2, 3, 9]))
print(quickSort([1]))
print(quickSort([]))
