# this is one to come back to
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        current = 0
        parentheses_to_close = 0
        for char in s:
            if char == '(':
                parentheses_to_close += 1
            elif parentheses_to_close:
                if parentheses_to_close == 1:
                    parentheses_to_close = 0
                    res = max(res,current)
                    current = 0
                parentheses_to_close -= 1
            else: continue
            current += 1
            res = max(res - parentheses_to_close, current)
        return res - parentheses_to_close
                


import timing

data = ["", "((())", "()()", "(", ")", "()(())((()))(())",
        "((((()((()))"]

classifiers = [0, 4, 2, 0, 0, 6, 6]

timing.batch(data, Solution().longestValidParentheses, classify=True, classifiers=classifiers)