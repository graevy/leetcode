# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

 

# Constraints:

#     1 <= s1.length, s2.length <= 104
#     s1 and s2 consist of lowercase English letters.

# first attempt failed because the iterator bounds-checking shortcut hit :-0,
# which does not result in the entire array, but instead an empty iterator. my fault

# second attempt failed because the first constraint does not actually
# specify that s1 <= s2. salty about that one

# third attempt succeeded, but is apparently really slow. 10th percentile
# i always score well on memory allocation but low on time. i probably missed something?
# i did. it's a sliding window problem. every substring problem is a sliding window problem
# god
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        from copy import deepcopy

        # build a string counter hashmap
        map = {}
        for char in s1:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1

        # if check_permutation is called, and it encounters an out-of-map character,
        # it shouldn't start from the next char in s2. it should skip some iterations
        # this brings the alg from linearithmic to linear worst-case
        skip_count = 0
        # to actually check permutations, copy the s1 hashmap and slowly destroy it.
        # destroying it prevents "hhhhhhlleo" from being a "hello" permutation
        # but preserves constant-time searching
        def check_permutation(candidate):
            string_counter = deepcopy(map)
            for idx,char in enumerate(candidate):
                if char in string_counter:
                    if string_counter[char] == 1:
                        del string_counter[char]
                    else:
                        string_counter[char] -= 1
                else:
                    skip_count = idx
                    return False
            return True

        # index is saved for string indexing, but also for shortcutting enumerate(s2).
        # by skipping the last few string characters, we don't have to check bounds
        # since the permutation checker expands rightward, there's no lost data
        iterator = enumerate(s2[:len(s2) - len(s1) + 1])
        for idx,char in iterator:
            if char in map:
                if check_permutation(s2[idx : idx + len(s1)]):
                    return True
                else:
                    for _ in range(skip_count):
                        next(iterator)
        return False

# passed all test cases
data = [("check","aaakechkec"),("ab","eidbaooo"),("ab","eidboaoo"),("test","test"),
("a","ab"),("a","ba"),("a","a"),("horse","ros")]
for point in data:
    print(Solution().checkInclusion(*point))