# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3

 

# Constraints:

#     The number of nodes in the tree is n.
#     1 <= k <= n <= 104
#     0 <= Node.val <= 104

 

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# first solution, sorted() means nlogn, there's probably a linear solution
class Solution:
    def kthSmallest(self, root: Optional[Node], k: int) -> int:
        def bfs(node,out):
            if node.left:
                bfs(node.left,out)
            if node.right:
                bfs(node.right,out)
            out.append(node.val)
            return out
        # guess who forgot BSTs store sorted data?
        return sorted([node for node in bfs(root,[]) if node is not None])[k-1]

# class Solution:
#     def kthSmallest(self, root: Optional[Node], k: int) -> int:
