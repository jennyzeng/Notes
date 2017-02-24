
"""
You are a professional robber planning to rob houses along a street.
 Each house has a certain amount of money stashed, the only constraint
 stopping you from robbing each of them is that adjacent houses have
 security system connected and it will automatically contact the
 police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of
money of each house, determine the maximum amount of money you
can rob tonight without alerting the police.
"""
class Solution(object):
	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		p(i) = max(p(i-2) + nums[i] or p(i-1))
		p(0) = nums[0]
		"""
		if not nums: return 0
		prev = 0
		cur = 0
		for i in nums:
			temp = cur
			cur = max(prev + i, cur)
			prev = temp
		return cur

	def rob2(self, nums):
		if not nums: return 0
		self.dp = [None] * (len(nums))
		self.dp[0] = nums[0]
		self.robDP(nums, len(nums) - 1)
		return self.dp[-1]

	def robDP(self, nums, i):
		if i < 0:
			return 0

		if self.dp[i] != None: return self.dp[i]

		self.dp[i] = max(self.robDP(nums, i - 2) + nums[i], self.robDP(nums, i - 2), self.robDP(nums, i - 1))

		return self.dp[i]


input = """
[0]
[1]
[2,3]
[1,2,3]
[0,1,-1,3,4,5,1]
"""
for i in input.strip().split('\n'):
	print(Solution().rob(eval(i)))
