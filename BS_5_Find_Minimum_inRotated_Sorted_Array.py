class Solution:

    # 二分法

    def find_minimum(self, nums):
        if nums is None:
            return -1

        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        return min(nums[start], nums[end])

## test case
if __name__ == '__main__':
    s = Solution()
    array = [1,2,3,4,5]
    print(s.find_minimum(array))