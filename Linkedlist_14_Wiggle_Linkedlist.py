'''
Given an unsorted array nums, reorder it in-place such that

nums[0] <= nums[1] >= nums[2] <= nums[3]....

Input: [3, 5, 2, 1, 6, 4]
Output: [1, 6, 2, 5, 3, 4]
'''

class Solution:
    def wiggle_linkedlist(self, nums):
        if not nums:
            return

        nums.sort()

        start = 0

        while start < len(nums) - 2:

            nums[start + 1], nums[start + 2] = nums[start + 2], nums[start + 1]

            start += 2

        return nums