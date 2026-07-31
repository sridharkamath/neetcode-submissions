class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        curr = []
        def dfs(i):
            if len(curr)==len(digits):
                res.append("".join(curr))
                return
            if i>=len(digits):
                return
            
            d = digits[i]
            for j in range(len(map[d])):
                curr.append(map[d][j])
                dfs(i+1)
                curr.pop()

                
        dfs(0)
        return res