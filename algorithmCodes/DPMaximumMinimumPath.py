"""
given a n*m matrix, there is a path p starts at matrix[0][0] and ends at matrix[len(matrix)-1][len(matrix[0]-1],
the path can only go down or right.
If the min value in p is p_m, find the maximum of all min values of paths in matrix.
e.g. matrix:
[8, 4, 7]
[6, 5, 9]
three paths:
8-4-7-9 min: 4
8-4-5-9 min: 4
8-6-5-9 min: 5
return 5
"""


class Solution:
	def findMaximumMinimumPath(self, matrix):
		if len(matrix[0]) == 0:
			return 0
		DP = self.makeTable(matrix)
		return DP[-1][-1]

	def makeTable(self, matrix):
		DP = [[None] * len(matrix[0]) for _ in range(len(matrix))]
		DP[0][0] = matrix[0][0]
		for i in range(1, len(matrix[0])):
			DP[0][i] = min(DP[0][i - 1], matrix[0][i])  # min of first row
		for i in range(1, len(matrix)):
			DP[i][0] = min(DP[i - 1][0], matrix[i][0])  # min of first col

		for i in range(1, len(matrix)):
			for j in range(1, len(matrix[0])):
				left = DP[i][j - 1]
				up = DP[i - 1][j]
				cur = matrix[i][j]
				if cur < left or cur < up:
					DP[i][j] = cur
				else:
					DP[i][j] = max(left, up)
		return DP


print(Solution().findMaximumMinimumPath([[]]))

matrix = [
	[8, 4, 7, 1]
]
print(Solution().findMaximumMinimumPath(matrix))  # 1

matrix = [
	[8, 4, 7],
	[6, 5, 9]
]
print(Solution().findMaximumMinimumPath(matrix))  # 5 because 8-6-5-9 = 5

matrix = [
	[8, 4, 7],
	[6, 5, 9],
	[6, 6, 6]
]
print(Solution().findMaximumMinimumPath(matrix))  # 6 because 8-6-6-6-6 = 6

matrix = [
	[8, 4, 7, 1],
	[9, 3, 2, 9],
	[7, 6, 6, 7],
	[3, 5, 4, 5]
]
print(Solution().findMaximumMinimumPath(matrix))  # 5 because 8-9-7-6-6-7-5 = 5

# time analysis: O(n). n is number of cells in matrix
