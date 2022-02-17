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


# first failure: consecutive asterisks in patterns didn't align properly
# second failure: c*b, ab
# third failure: .*c, ab
# sometimes, when solving a problem, the answer is going to lie more in the test suite than the algorithm
# lesson learned
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # which index of the string s do we care about?
        # don't use enumerate, because in some asterisk cases, its indexing stops lining up with p.
        idx = 0
        current_char = p[0]
        
        # loop through p, but test the previous character after confirming it's not followed by an asterisk
        # junk data added onto the end of p, so the last character is included in that iteration
        for next_char in (p + ' ')[1:]:
            # if we hit an asterisk, it's junk data, because we already looked at the previous character
            # this allows us to skip consecutive asterisks
            if current_char == '*':
                pass
            # if the next char is an asterisk, we have to loop through s until we hit a not-previous-character
            elif next_char == '*':
                for asterisk_char in s[idx:]:
                    if asterisk_char == current_char:
                        idx += 1
                    else: break
            # the base case
            elif current_char == s[idx] or current_char == '.':
                idx += 1
            # if there's a single pattern character mismatch, we already know it's not followed by an asterisk;
            # we can return False safely
            else:
                return False

            current_char = next_char 

        # lastly, if there are more characters in s after we've exhausted p, it's not a valid pattern match
        return True if idx == len(s) else False

data = [
    (('hellooooook', 'hel.o*'),False), (('helloooooo', 'hel.o*'),True),
    (('ab','a'),False), (("test","t.*"),True), (("hhellooh","h*el*o*."),True),
    (("mississippi","mis*is*ip*."),True), (("x","i***"),False), (("x","x***"),True),
    (("aab","c*a*b"),True), (("ab",".*c"), False)
    ]

# for point in data:
#     if Solution().isMatch(*point[0]) != point[1]:
#         print(str(point) + " failure.")

print(Solution().isMatch("test","t.*"))