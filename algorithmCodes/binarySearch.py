"""
binary search
1. could be used to look up keys(exact match),
but almost always worse than hashing
2. actually useful for approximate matching
	e.g. find nearest(or next smaller or next larger) key in your data set to a query

"""


def binarySearch(A, low, high, q):
	# find position of q in A[low]...A[high]
	if low >= high: return low
	mid = (low + high) // 2
	if q < A[mid]:
		return binarySearch(A, low, mid - 1, q)  # recurse in left subtree
	elif q > A[mid]:
		return binarySearch(A, mid + 1, high, q)  # recurse in right subtree
	return mid


# time analysis: O(log n)

print(binarySearch([1, 2, 3, 4, 5, 6], 0, 5, 5))  # 4
print(binarySearch([], 0, 0, 1))  # 0


class binaryTree:
	def __init__(self):
		self.value = None
		self.left = None
		self.right = None

	def left(self):
		return self.left

	def right(self):
		return self.right

	def value(self):
		return self.value


"""
notes:
1. it works well when you can sort the data once, and it doesn't change after that.
2. what about when data can change by adding and removing values? use binary search trees
tree whose paths represent sequences of comparisons made by binary search algorithm
"""


def binarySearch(tree, x):
	if not tree:  # is external node
		return tree
	elif tree.value() > x:
		return binarySearch(tree.left(), x)
	elif tree.value() and tree.right() < x:
		return binarySearch(tree.right(), x)
	else:
		return tree


"""
advantage of having external nodes:
even when you don't find x, return useful info(where x should go if inserted)
worst case:
O(longest root-leaf path length
goal:
keep tree balanced so this is O(log n)
use AVL tree or WAVL tree
I will implement them in the future...
"""
