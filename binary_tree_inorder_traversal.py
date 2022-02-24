# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:

# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:

# Input: root = []
# Output: []

# Example 3:

# Input: root = [1]
# Output: [1]

# Constraints:

#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# honestly it was faster to just debug than try to build this
# class Tree:
#     def __init__(self, root: TreeNode, size=0):
#         self.root = root
#         self.size = size
#     def add_



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def recur(node):
            if node.left:
                recur(node.left)
                
            res.append(node.val)

            if node.right:
                recur(node.right)

        if root:
            recur(root)
        return res