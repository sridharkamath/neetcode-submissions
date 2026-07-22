# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def maxHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        lh = self.maxHeight(node.left)
        rh = self.maxHeight(node.right)

        self.diameter = max(self.diameter,lh+rh)

        return 1+max(lh,rh)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        mh = self.maxHeight(root)

        return self.diameter
        
    