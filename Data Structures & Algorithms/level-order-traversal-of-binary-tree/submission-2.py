# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        s = deque()
        s.append(root)
        curr_l=1
        while s:
            curr = []
            l = 0
            for _ in range(curr_l):
                if s:
                    n=s.popleft()
                    if n:
                        curr.append(n.val)
                        if n.left:
                            s.append(n.left)
                            l+=1
                        if n.right:
                            s.append(n.right)
                            l+=1
            curr_l = l
            if curr:
                res.append(curr)
        return res