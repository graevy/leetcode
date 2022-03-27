# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.

# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.

 

# Constraints:

#     -2**31 <= dividend, divisor <= 2**31 - 1
#     divisor != 0


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(divisor) > abs(dividend):
            return 0

        # ah, it's a close code block, but it's a terrible way to actually divide
        while divisor > 1:
            if divisor & 1:
                dividend -= divisor
            dividend = dividend >> 1
            divisor = divisor >> 1

        dividend = quotient

        if quotient < 0:
            quotient += 1

        if quotient < -2 ** 31:
            quotient = -2**31
        elif quotient > 2**31 - 1:
            quotient = 2**31 - 1

        return quotient

    def divide2(self, dividend: int, divisor: int) -> int:
        pass

    # it's close, but too lossy
    # def divide3(self, dividend, divisor):
    #     return dividend >> (divisor.bit_length() - 1)



data = [(2,5), (5,2), (-2, 5), (-5,2), (4,1), (4,2), (1,1), (0,1), (31,12), (-23443, 12039874), (999999999999999, 7)]
# data = [(-5,2)]
classifiers = [int(x/y) for x,y in data]

from timing import batch
batch([Solution().divide, Solution().divide2], data, classifiers=classifiers, unpack_data=True)

# print(Solution().divide(-5,2))