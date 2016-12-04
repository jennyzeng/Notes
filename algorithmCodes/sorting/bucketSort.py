"""
cs161 note9
faster sorting by avoiding comparison-based algorithm
1. why?
	- slow. If can only compare -- n log n is best
2. Integer sorting
input: n objects with integer keys in range 0...N-1 (N different values)

Bucket sort: O(n+N)
not a stable sort
"""


def bucketSort(items, N):
	buckets = [[] for _ in range(N)]
	print(buckets)
	for i in items:
		buckets[items[i]].append(i)
	result = []
	for bucket in buckets:
		for item in bucket:
			result.append(item)
	return result

items = {"A": 0, "B": 1, "C": 0, "D": 0, "E": 2, "F": 0, "G": 4,
         "H": 2, "I": 1, "J": 2, "K": 0}
N = 5

print(bucketSort(items, N))
