# Give a sorted array: A [ ]
# A non-negative integer: K
# A Target

# 找出数组A 中 距离Target 最近的K个数
# 先二分法 再双指针
# 第一 是否左指针小于0，如果小于0，右指针走
# 第二 是否右指针大于数组的长度，如果大于，左指针走
# 第三 判断 左指针与target的距离 和target到右指针的距离
class Solution:

    def closest_numbers(self, A, target, k):

        index = self.find_Index(A, target)

        result = []
        left, right = index -1, index

        for i in range(k):
            if left < 0:
                result.append(A[right])
                right += 1
            elif right == len(A):
                result.append(A[left])
                left -= 1
            else:
                if target - A[left] <= A[right] - target:
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1

    def find_Index(self, A, target):
        '''
        :param A: The Array
        :param target: The target
        :return: return the place of index
        '''
        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return len(A)