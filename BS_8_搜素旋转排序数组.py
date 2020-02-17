class Solution:
    def search_in_rotated_array(self, A, target):
        # 旋转数组
        if not A:
            return -1

        start, end = 0, len(A) - 1

        while start + 1< end:

            mid = (start + end) // 2

            if A[mid] >= A[start]:

                if A[start] <= target <= A[mid]:

                    end = mid

                else:
                    start = mid
            else:

                if A[mid] <= target <= A[end]:
                    start = mid

                else:
                    end = mid

        if A[start] == target:
            return start

        if A[end] == target:
            return end

        return -1
