"""
LeetCode 416, Partition Equal Subset Sum
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

similar to 0/1 knapsack problem
take or do not take
"""


def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    numsum = sum(nums)
    if numsum % 2: return False
    sub_sum = numsum / 2

    dp = [[False] * (sub_sum + 1) for _ in range(len(nums) + 1)]

    dp[0][0] = True  # base case when take none and sum is none

    for i in range(1, len(nums) + 1):  # sum is 0 and take none
        dp[i][0] = True

    for j in range(1, sub_sum + 1):  # sum is more than 0 but take none
        dp[0][j] = False

    for i in range(1, len(nums) + 1):
        for j in range(1, sub_sum + 1):
            dp[i][j] = dp[i - 1][j]  # without taking num[i-1]
            if j - nums[i - 1] >= 0:
                # take this item or not
                # it goes back to the situation when we have nums[:i-2] and the result of it
                dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]

    return dp[-1][-1]

"""
use only one dimension dp to save space
"""
def canPartition1(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    numsum = sum(nums)
    if numsum & 1: return False
    sub_sum = numsum / 2

    dp = [False for _ in range(sub_sum + 1)]
    dp[0] = True
    for num in nums:
        for i in range(sub_sum, 0, -1):
            if i >= num:
                dp[i] = dp[i] or dp[i - num]

    return dp[-1]


if __name__ == '__main__':
    assert canPartition1([1,2,5]) == False
