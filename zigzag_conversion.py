# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

 

# Constraints:

#     1 <= s.length <= 1000
#     s consists of English letters (lower-case and upper-case), ',' and '.'.
#     1 <= numRows <= 1000


# horrible algorithm but it worked second try. it failed where numRows==1 so guess how i addressed that
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        up = 1
        current = 0
        positions = [] 
        max_row = numRows-1
        for char in s:
            if current == max_row:
                up = -1
            elif current == 0:
                up = 1
            positions.append(current)
            current += up

        rows = [[] for _ in range(numRows)]
        for idx,i in enumerate(positions):
            rows[i].append(s[idx])

        return ''.join(char for row in rows for char in row)

print(Solution().convert(s='ABC',numRows=1))