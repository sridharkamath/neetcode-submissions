# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def dfs(self, node, minval, maxval):
        if not node:
            return True
        
        if node.val>=maxval or node.val<=minval:
            return False
        
        return self.dfs(node.left,minval,min(maxval,node.val)) and self.dfs(node.right,max(minval,node.val),maxval)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.dfs(root.left, float("-inf"), root.val) and self.dfs(root.right, root.val, float("inf"))
        

            
