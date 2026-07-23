# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = True

    def getHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        lh = self.getHeight(node.left)
        rh = self.getHeight(node.right)

        if abs(lh-rh)>1:
            self.res=False
        
        return 1+max(lh,rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return self.res
        
        res = self.getHeight(root)

        return self.res

