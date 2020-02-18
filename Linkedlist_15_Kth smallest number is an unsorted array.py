class Solution:
    def kth_smallest_number(self, nums, k):
        return self.quick_sort(nums, 0, len(nums)-1, k)

    def quick_sort(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(start + end) // 2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums[k-1]

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,4,2,7]
    k = 3
    print(s.kth_smallest_number(nums, k))