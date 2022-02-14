# We define the usage of capitals in a word to be right when one of the following cases holds:

#     All letters in this word are capitals, like "USA".
#     All letters in this word are not capitals, like "leetcode".
#     Only the first letter in this word is capital, like "Google".

# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true

# Example 2:

# Input: word = "FlaG"
# Output: false

 

# Constraints:

#     1 <= word.length <= 100
#     word consists of lowercase and uppercase English letters.

# second try. first try i put the wrong var in the loops. less than 3 minutes
# new medium pb
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
            return True
        if 64 < ord(word[0]) < 91:
            if 64 < ord(word[1]) < 91:
                for char in word[2:]:
                    if 96 < ord(char) < 123:
                        return False
                return True
            else:
                for char in word[2:]:
                     if 64 < ord(char) < 91:
                            return False
                return True
        else:
            for char in word[1:]:
                if 64 < ord(char) < 91:
                    return False
            return True