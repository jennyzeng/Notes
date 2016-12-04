# Merge sort, a O(nlogn) algorithm, is stable sort
def mergeSort(L):
	if len(L) <= 1:
		return L
	else:
		mid = len(L) // 2
		left = mergeSort(L[:mid])
		right = mergeSort(L[mid:])
		return merge(left, right)


def merge(left, right):
	L = []
	i = 0  # for left
	j = 0  # for right
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			L.append(left[i])
			i += 1
		else:
			L.append(right[j])
			j += 1
	L += (left[i:] if i < len(left) else []) + (right[j:] if j < len(right) else [])
	return L


## test
test1 = [2, 5, 1, 0, 6, 3, 9, 7]
print(mergeSort(test1))
test2 = [1, 2, 3, 4, 5, 7, 9]
print(mergeSort(test2))
print(mergeSort([2, 3, 2, 4, 2, 3, 1]))
print(mergeSort([-2, -3, 2, -4, 2, 3, 1]))
print(mergeSort([3,2]))
print(mergeSort([0]))
print(mergeSort([]))
