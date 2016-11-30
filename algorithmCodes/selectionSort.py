"""
selection sort algorithm
- "comparison sorting"
- input: collection of objects that can be compared in pairs to give a single consistent ordering
- output: objects in sorted order
"""


def selectionSort(X):
	output = []
	while X:
		minEle = None
		for ele in X:   # loop through X to find min, time O(n)
			if not minEle or minEle > ele:
				minEle = ele
		output.append(minEle)   # move this ele to output, constant time, O(1)
		X.remove(minEle)
	return output


print(selectionSort([4, 2, 23, 1, 2, 0, -1]))
"""
Time analysis:
- # iterations of inner loop = (n)+(n-1)+(n-2)+...+2+1=n(n-1)/2 = O(n^2)
Key steps in selection sort
- find and remove min of X
	happens n times => O(n^2) total time
	all other parts of the algorithm => O(n) time
"""