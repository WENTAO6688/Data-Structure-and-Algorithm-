class Solution:
    def quick_power(self, a, b, n):
        '''
        :param a: the 32 bit base
        :param b: divisor
        :param n: the 32 bit exponent
        :return:
        '''
        if n == 0:
            return 1 % n
        if n == 1:
            return a % b

        power = self.quick_power(a, b, n//2)
        power = (power * power) % b

        if n % 2 == 1:
            power = (power * a) % b

        return power
