"""
Binary Heap
Definition:
	store our items as an array. e.g X[0],X[1],..
	 but we think of it as a (binary) tree
	        X[0]
		/          \
	X[1]            X[2]
	/   \           /   \
X[3]    X[4]      X[5]  ...

parent of X[i]: X[ floor( (i-1)/2 )]
Children of X[i]: X[2i+1], X[2i+2]
require that value(parent) < value(child)   ---- min heap

- to find the min:
	look at X[0]  ---> O(1)

- to remove the min:
	swap X[0] with last item X[n-1]
	n = n-1
	do heapify ---> O(logn)

- to insert an element into a heap
	- add at end of array
	- repeatedly swap upwards (heapify) --> O(logn)

- to create a heap from an unordered array:
	sum^{n}_{0}(log(#descs of X[i]) = O(n)

"""


class binaryHeap:
	def __init__(self):
		self._L = []

	def __str__(self):
		return str(self._L)

	def getMin(self):  # O(1)
		return self._L[0] if len(self._L) > 0 else None

	def removeMin(self):  # O(log n)
		self._swap(0, len(self._L) - 1)
		del self._L[-1]
		self._heapify(0)  # index 0: the out-of -place element that we just moved

	def insert(self, x):  # O(log n)
		self._L.append(x)  # add at end of array
		for i in range((len(self._L) - 1) // 2, -1, -1):
			self._heapify(i)  # repeatedly swap upwards

	def create(self, A):
		self._L = A
		for i in range((len(self._L) - 1) // 2, -1, -1):  # for i = n-1, n-2,..., 0:
			self._heapify(i)  # swap downwards, starting from L[i]

	def _left(self, i):  # left child of i
		return 2 * i + 1

	def _right(self, i):  # right child of i
		return 2 * i + 2

	def _parent(self, i):  # parent of i
		return (i - 1) // 2

	def _heapify(self, i):  # swapping process starting from i. go downward
		parent = i
		while True:
			left = self._left(parent)
			right = self._right(parent)
			smallest = None
			if left < len(self._L) and self._L[left] < self._L[parent]:
				smallest = left
			else:
				smallest = parent
			if right < len(self._L) and self._L[right] < self._L[smallest]:
				smallest = right

			if smallest != parent:
				self._swap(smallest, parent)
				parent = smallest  # swapped, this become the smallest one
			else:
				break

	def _swap(self, a, b):
		self._L[a], self._L[b] = self._L[b], self._L[a]


## test
heap = binaryHeap()
heap.create([3, 1, 9, 6, 2, 5])  # [1,2,5,6,3,9]
print("create heap: ", heap)
heap.insert(7)  # [1, 2, 5, 6, 3, 9, 7]
print("insert 7:", heap)
heap.insert(0)  # [0, 1, 5, 2, 3, 9, 7, 6]
print("insert 0: ", heap)
heap.removeMin()  # [1, 2, 5, 6, 3, 9, 7]
print("removeMin: ", heap)
heap.removeMin()  # [2, 3, 5, 6, 7, 9]
print("removeMin: ", heap)
