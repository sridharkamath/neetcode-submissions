class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        close=n
        open=n
        curr = []
        res = []
        def dfs(o,c):
            if len(curr)==(2*n):
                res.append("".join(curr))
                return
            if o:
                curr.append("(")
                dfs(o-1,c)
                curr.pop()
            if c>o:
                curr.append(")")
                dfs(o,c-1)
                curr.pop()
        dfs(open,close)
        return res
            