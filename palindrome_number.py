class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        if x < 0:
            return False
        if x == 0:
            return True
        digits = []
        for _ in range(int(math.log(x,10)) + 1):
            digits.append(x % 10)
            x //= 10
        for idx,digit in enumerate(reversed(digits)):
            if digit != digits[idx]:
                return False
        return True
        
# print(Solution().isPalindrome(123454321))
print(Solution().isPalindrome(567))
print(Solution().isPalindrome(-1234321))