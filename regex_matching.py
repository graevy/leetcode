# 10. Regular Expression Matching
# Hard

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

#     '.' Matches any single character.​​​​
#     '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

 

# Example 1:

# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:

# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:

# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

 

# Constraints:

#     1 <= s.length <= 20
#     1 <= p.length <= 30
#     s contains only lowercase English letters.
#     p contains only lowercase English letters, '.', and '*'.
#     It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # which index of the string s do we care about?
        # don't use enumerate, because in some asterisk cases, it stops lining up with p.
        idx = 0
        
        iterator = iter(p)
        for char in iterator:

            if char == s[idx] or char == '.':
                idx += 1
                continue
            if char == '*':
                try:
                    for asterisk_char in s[idx+1:]
                        

            # if char == s[idx] or char == '.':
            #     idx += 1
            #     continue

            # try:
            #     if p[idx] == '*':

            #         # if our string so far is valid .* means the rest is automatically valid
            #         if char == '.':
            #             return True
            #         # consecutive asterisks are functionally 1 asterisk, so the loop can next_char_is_asterisk_boolreak here
            #         if char == '*':
            #             continue

            #         for asterisk_char in s[idx:]:
            #             if asterisk_char == char:
            #                 idx += 1
            #             else:
            #                 break
            #         next(iterator)

            # except IndexError: 
            #     pass

            # return False

        if idx != len(s):
            return False
        else:
            return True

data = [
    (('hellooooook', 'hel.o*'),False), (('helloooooo', 'hel.o*'),True),
    (('ab','a'),False), (("test","t.*"),True), (("hhellooh","h*el*o*."),False),
    (("mississippi","mis*is*ip*."),True), (("x","i***"),False), (("x","x***"),True),
    (("aab","c*a*b"),True)
    ]

for point in data:
    if Solution().isMatch(*point[0]) != point[1]:
        print(str(point) + " failure.")

# print(Solution().isMatch("mississippi","mis*is*ip*."))