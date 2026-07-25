# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, node, count, max_val):
        if not node:
            return 0
        
        if node.val >= max_val:
            max_val = node.val
            self.count+=1

        if node.left:
            self.dfs(node.left, self.count, max_val)
        if node.right:
            self.dfs(node.right, self.count, max_val)


    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_val = root.val
        self.dfs(root, self.count, max_val)

        return self.count