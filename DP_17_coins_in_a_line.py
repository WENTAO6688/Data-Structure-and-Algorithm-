'''
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left.
The player who take the last coin wins.
Could you please decide the first player will win or lose?
If the first player wins, return true, otherwise return false.
'''
'''
follow-up:
O(1) time complexity and O(1) space complexity 
'''
'''
T T F T T F T T F
1 2 3 4 5 6 7 8 9
规律是最后一个 == not(前一个 and 后一个)
'''
class Solution:
    def who_will_wins(self, number_of_coins):
        # 没硬币
        if not number_of_coins:
            return False

        # 只要有1或者2个 绝对赢
        if number_of_coins < 3:
            return True

        # 如果硬币大于等于3
        this_1, this_2, this_3 = True, True, False

        for _ in range(2, number_of_coins):

            this_3 = not (this_1 and this_2)
            # 更新 this_1 and this_2
            this_1, this_2 = this_2, this_3

        return this_3

if __name__ == "__main__":
    s = Solution()
    print(s.who_will_wins(8))