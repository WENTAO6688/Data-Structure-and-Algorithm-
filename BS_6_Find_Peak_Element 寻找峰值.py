class Solution:
    def find_peak(self, nums):
        '''
        :param nums: the array
        :return:
        '''
        start, end = 1, len(nums) - 2

        while start + 1 < end:
            mid = (start + end)  // 2
            if nums[mid] < nums[mid-1]:
                end = mid
            if nums[mid] < nums[mid+1]:
                start = mid
            else:
                end = mid

        if nums[start] < nums[end]:
            return end
        else:
            return start
