class Solution:

    def mountainSequence(self, nums):
        start, end = 0, len(nums) -1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid
        return max(nums[start], nums[end])
    