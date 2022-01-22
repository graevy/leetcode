# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

 

# Constraints:

#     1 <= strs.length <= 200
#     0 <= strs[i].length <= 200
#     strs[i] consists of only lower-case English letters.


# this one took 4 tries ;-;

def longestCommonPrefix(strs: list[str]) -> str:
    out = strs[0]
    for string in strs[1:]:
        if string[:len(out)] != out:
            out = out[:len(string)]
            for idx,character in enumerate(string):
                if character != out[idx]:
                    out = out[:idx]
                    break

    return out

print(longestCommonPrefix(["ab","a"]))