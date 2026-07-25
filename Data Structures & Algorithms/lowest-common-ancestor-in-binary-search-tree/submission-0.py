# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        lac = root
        l = p if p.val>q.val else q
        s = p if p.val<q.val else q

        if s.val<=root.val and l.val>=root.val:
            lac = root
        else:
            if l.val<root.val:
                lac = self.lowestCommonAncestor(root.left,l,s)
            elif s.val>root.val:
                lac = self.lowestCommonAncestor(root.right,l,s)

        return lac



