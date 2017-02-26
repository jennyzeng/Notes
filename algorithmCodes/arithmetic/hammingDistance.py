# leetcode 461, hamming distance

class Solution(object):
	def hammingDistance(self, x, y):
		"""
		:type x: int
		:type y: int
		:rtype: int
		"""
		res = 0
		while not (x == 0 and y == 0):
			if x & 1 != y & 1:
				res += 1
			x = x >> 1
			y = y >> 1
		return res


assert Solution().hammingDistance(1, 4) == 2
