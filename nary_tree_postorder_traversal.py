"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        def recur(node):
            for child in node.children:
                recur(child)
                
            res.append(node.val)

        if root:
            recur(root)
        return res