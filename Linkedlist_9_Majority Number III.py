class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        n = len(nums)

        count_limit = n / k

        hash = {}

        for i in range(n):

            if nums[i] in hash:

                hash[nums[i]] += 1

            else:

                hash[nums[i]] = 1

        for keys in hash.keys():

            if hash[keys] > count_limit:

                return keys
"time complexity: O(n^2)"
if __name__ == "__main__":
    s = Solution()
    nums = [3,1,2,3,2,3,3,4,4,4]
    k = 3
    print(s.majorityNumber(nums, k))
