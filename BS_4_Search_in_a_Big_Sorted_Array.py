# 从一个升序的数组中 求出第一次出现target的下标
# [1, 2, 3, 3, 3, 6, 7, 7, 8, 9, 10]
# if we want to find 7
class Solution:
    def find_index_of_target(self, reader, target):

        # 问题的关键在于我们并不知道数组的长度是多少
        # 但end一定是要大于等于target的
        start = 0
        end = 1
        while reader.get(end) < target:
            end = end * 2

        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start

        if reader.get(end) == target:
            return end

        return -1





