# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        s=deque()
        s.append(root)
        while s:
            l = len(s)
            if l == 1:
                n = s.popleft()
                res.append(n.val)
                if n.left:
                    s.append(n.left)
                if n.right:
                    s.append(n.right)
            else:
                for _ in range(len(s)-1):
                    n = s.popleft()
                    if n.left:
                        s.append(n.left)
                    if n.right:
                        s.append(n.right)
                n = s.popleft()
                res.append(n.val)
                if n.left:
                    s.append(n.left)
                if n.right:
                    s.append(n.right)
        return res