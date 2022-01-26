# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

# Example 1:

# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]

# Example 2:

# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]

 

# Constraints:

#     The number of nodes in each tree is in the range [0, 5000].
#     -105 <= Node.val <= 105

# 3 minute solution new medium record!
# apparently faster than 97% of python solutions. weird
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def bfs(node, out):
            if node.left:
                bfs(node.left, out)
            if node.right:
                bfs(node.right, out)
            out.append(node.val)
            return out
        return sorted((bfs(root1,[]) if root1 else []) + (bfs(root2,[]) if root2 else []))