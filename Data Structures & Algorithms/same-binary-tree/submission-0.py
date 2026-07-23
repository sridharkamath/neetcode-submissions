# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        stack = [[p,q]]
        while stack:
            a,b = stack.pop()

            if (not a and b) or (a and not b):
                res = False
                break
            elif a and b:
                if a.val != b.val:
                    res = False
                    break
                else:
                    stack.append([a.left,b.left])
                    stack.append([a.right,b.right])
        
        return res
        
