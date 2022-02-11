# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

# Constraints:

#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.


# my first solution here is O(n) because of window sliding. it's just slow.
# python dict is used over set because order is preserved.
# what this solution needs is an order-preserving hash with a left-removal method
# the faster solutions to this problem maintain character indices instead of cleaning the dict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = {}
        result = 0

        for char in s:
            # if the character's in the substring, delete everything up to and including it
            if char in substring:
                for key in substring.copy():
                    del substring[key]
                    if key == char: break

            substring[char] = None

            if len(substring) > result:
                result = len(substring)
        
        return result

tests = ['', '12ad', 'bbbbbbb', 'abac', 'abcdabcabcdeabcdabc', [chr(i) for i in range(48,123)]*1000]
for test in tests:
    print(Solution().lengthOfLongestSubstring(test))
