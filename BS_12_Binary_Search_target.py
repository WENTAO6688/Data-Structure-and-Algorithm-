class Solution:

    def Binary_Search(self, nums, target):
        """
        :param nums: the integer array
        :param target: target number to find
        :return:first position of target
        """
    # example: [1,   2,   3,   6,   7,   7,   10]
    # position: 0    1    2    3    4    5    6
    # 解题思路：
    # 1. when nums is none or null, return -1
    # 2. if not, create two pointers: left and right

        left, right = 0, len(nums)-1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                # nums[mid] > target
                right = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        return -1


# Practice
# class Solution:
#     def BinarySearch(self, nums, target):
#         # define left and right
#         left, right = 0, len(nums)-1
#         while left + 1 < right:
#             mid = (left + right) // 2
#             if nums[mid] > target:
#                 right = mid
#             else:
#                 left = mid
#         if nums[left] == target:
#             return left
#         elif nums[right] == target:
#             return right
#         return -1



