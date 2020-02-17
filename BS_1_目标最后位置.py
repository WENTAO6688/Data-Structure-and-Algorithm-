# 给定一个数组
# 求出数组中最后出现target的下标
# 若不存在 返回 -1

class Solution:
    def find_target(self, nums, target):

        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                start = mid

        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        else:
            return -1