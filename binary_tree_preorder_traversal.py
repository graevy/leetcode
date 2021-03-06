# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def recur(node):
            res.append(node.val)

            if node.left:
                recur(node.left)

            if node.right:
                recur(node.right)

        if root:
            recur(root)
        return res