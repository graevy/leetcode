# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

 

# Constraints:

#     n == height.length
#     1 <= n <= 2 * 104
#     0 <= height[i] <= 105


# this doesn't account for water getting trapped in buckets-in-buckets at the end of the array
# i bet linear is still possible though
class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0
        current_bucket = 0
        current_height = 0
        for considered_height in height:
            if considered_height >= current_height:
                current_height = considered_height
                total += current_bucket
                current_bucket = 0
            else:
                current_bucket += current_height - considered_height
                
        return total

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))