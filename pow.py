# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 
# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:

# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:

# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

 

# Constraints:

#     -100.0 < x < 100.0
#     -2**31 <= n <= 2**31-1
#     -10**4 <= x**n <= 10**4

import math
import timing

class Solution:
    @staticmethod
    # wanted to do this without math.log
    # "most significant bit"
    def get_msb(x):
        msb = 1
        for _ in range(x.bit_length()-1):
            msb *= 2
        return msb

    # make the worst alg first
    @timing.timed
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        base = x
        for e in range(abs(n) - 1):
            x *= base
        return x if base > 0 else 1/x
    
    # i think this counts as log(n)
    # actually disappointed by how slow this is

    # first submission success :) 59th speed, 99th memory
    # shoutout to the 10% of submissions that were just "return x**n"
    @timing.timed
    def my_pow_2(self, x, n):
        if n == 0: return 1

        negative = True if n < 0 else False
        n = abs(n)
        base = x
        out = 1
        while n > 0:
            for _ in range(n.bit_length() - 1):
                x *= x
            out *= x
            x = base
            n -= Solution.get_msb(n)

        return 1/out if negative else out

    
data = [(5,240), (-3,7), (13,-12), (2,10), (2.1,3), (2,-2), (5,0), (1,-5), (0,0)]
classifiers = [x**y for x,y in data]
for point,classifier in zip(data, classifiers):
    Solution().my_pow_2(*point, classify=True, classifier=classifier)
