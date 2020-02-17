'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
Find the minimum element.

Input :[2,1]
Output : 1.

Input :[4,4,5,6,7,0,1,2]
Output : 0.
'''

class Solution:

    def find_minimum(self, nums):

        if not nums:

            return

        if len(nums) ==  1:

            return nums[0]

        return self.helper(nums)

    def helper(self, nums):

        start, end = 0, len(nums) - 1

        while start < end:

            mid = (start + end) // 2

            if nums[mid] > nums[end]:

                start = mid + 1

            elif nums[mid] < nums[end]:

                end = mid

            else:
                # nums[mid] == nums[end]
                end -= 1

        return nums[0]

