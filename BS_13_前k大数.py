# 在一个数组中找到前K大的数

class Solution:

    def Klargest_numbers(self, k, nums):
        # edge condition
        if nums is None or len(nums) == 0 or k < 1 or k > len(nums):
            return None

        return self.partition(nums, 0, len(nums)-1, len(nums)-k)

    def partition(self, nums, start, end, k):

        if start == end:
            return self.sortReverse(nums)
        # two pointers
        left, right = start, end
        mid = (left + right) // 2
        while left < right:
            while left < right and nums[left] < nums[mid]:
                left += 1
            while left < right and nums[right] > nums[mid]:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= right:
            return self.partition(nums, left, end, k)

        return self.sortReverse(nums[k:])

    def sortReverse(self, nums):
        nums.sort()
        nums.reverse()
        return nums

