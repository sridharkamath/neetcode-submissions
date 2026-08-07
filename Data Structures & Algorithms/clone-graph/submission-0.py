"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hm = defaultdict(List)
        def dfs(v):
            if v in hm:
                return
            new = Node(v.val)
            hm[v] = new

            for n in v.neighbors:
                dfs(n)
                hm[v].neighbors.append(hm[n])
        dfs(node)
        return hm[node]