# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

 
# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

 

# Constraints:

#     1 <= s.length <= 10**4
#     s consists of parentheses only '()[]{}'.


# no mistakes, but a straightforward problem that begs for a stack
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        syntax = {'{':'}', '(':')', '[':']'}
        try:
            for char in s:
                if char in syntax:
                    stack.append(char)
                elif char == syntax[stack.pop()]:
                    continue
                else:
                    return False
            return True if not stack else False

        except:
            return False


import timing
data = ['', '(', '(]', '()', '(())', '([])', '([)]', '{[]()}', '{[](){}']
classifiers = [True, False, False, True, True, True, False, True, False]

timing.batch([Solution().isValid], data, classifiers)
