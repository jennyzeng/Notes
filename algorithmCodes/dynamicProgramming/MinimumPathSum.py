"""
Given a m x n grid filled with non-negative numbers, find a path from top
left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""
import matrixHelper as mh


class Solution(object):
	def minPathSum(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""

		if len(grid) == 1:
			return sum(grid[0])

		DP = self.createTable(grid)
		return DP[-1][-1]




	def createTable(self, grid):
		DP = mh.createDP(grid)
		DP[0][0] = grid[0][0]
		for i in range(1, len(grid)):
			DP[i][0] = DP[i - 1][0] + grid[i][0]
		for j in range(1, len(grid[0])):
			DP[0][j] = DP[0][j - 1] + grid[0][j]

		for j in range(1, len(grid[0])):
			for i in range(1, len(grid)):
				DP[i][j] = min(DP[i - 1][j], DP[i][j - 1]) + matrix[i][j]
		return DP

matrix = \
	[
		[3,2,4,0],
		[5,6,3,1],
		[4,3,2,3]
	]

DP = Solution().createTable(matrix)
mh.printMatrix(DP)

assert 13==Solution().minPathSum(matrix)
assert 0==Solution().minPathSum([[]])
assert 6==Solution().minPathSum([[1,2,3]])
