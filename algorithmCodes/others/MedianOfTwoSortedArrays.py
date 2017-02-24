
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

Submission Details
2080 / 2080 test cases passed.
Status: Accepted
Runtime: 85 ms
Your runtime beats 96.53% of python submissions.
"""


class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: float
		"""
		i = 0
		j = 0
		mid = (len(nums1) + len(nums2)) // 2 + 1
		last = None
		secondLast = None
		while i + j < mid:

			if i >= len(nums1) and j >= len(nums2):
				break

			secondLast = last
			if i >= len(nums1):
				last = nums2[j]
				j += 1

			elif j >= len(nums2):
				last = nums1[i]
				i += 1

			elif nums1[i] < nums2[j]:

				last = nums1[i]
				i += 1
			else:
				last = nums2[j]
				j += 1

		if (len(nums1) + len(nums2)) % 2 == 0:
			return float(last + secondLast) / 2
		else:
			return last

print(Solution().findMedianSortedArrays([1,3], [2]))
print(Solution().findMedianSortedArrays([1,2], [3,4]))

