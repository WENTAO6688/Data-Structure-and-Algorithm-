'''
["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
输出： 3
我们可以有如下三种方式：
"CatMat" = "Cat" + "Mat" | "CatMat" = "Ca" + "tM" + "at"  | "CatMat" = "C" + "at" + "Mat"
'''
class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, string, dict):

        if not string or not dict:
            return 0

        dict_lower = set()

        for words in dict:

            dict_lower.add(words.lower())

        n = len(string)

        # create the list for storing elements
        dp = [0 for _ in range(n+1)]
        # initialization
        dp[0] = 1

        for i in range(1, n+1):

            for j in range(0, i):

                if string[j:i].lower() in dict:

                    dp[i] += dp[j]

        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    string = 'helloworld'
    dict = ['he','llo','world','hello','world']
    print(s.wordBreak3(string, dict))




