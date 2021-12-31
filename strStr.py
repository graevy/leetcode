def traverse(haystack, needle):
    if not needle:
        return 0
    for idx,elem in enumerate(haystack):
        # print(idx,elem)
        if elem == needle[0]:
            # print('reached' + str(elem))
            try:
                assert haystack[idx:idx+len(needle)] == needle
                return idx
            except: pass
    return -1

def again(h,n):
    # looked up the alg to do this. knuth-morris-pratt, O(n+k). if i come back to this i want to write this one out
    pass

print(traverse('hello','ll')) # first try success! i did this in 5 minutes. personal best


# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Example 3:

# Input: haystack = "", needle = ""
# Output: 0

 

# Constraints:

#     0 <= haystack.length, needle.length <= 5 * 104
#     haystack and needle consist of only lower-case English characters.
