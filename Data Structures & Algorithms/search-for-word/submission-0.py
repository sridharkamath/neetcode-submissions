class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        root = TrieNode()
        curr = root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.isWord = True

        res = False
        row = len(board)
        col = len(board[0])

        def dfs(i,j,curr):
            nonlocal res
            if i<0 or j<0 or i>=row or j>=col:
                return

            ch = board[i][j]

            if ch=="#":
                return
            
            if ch not in curr.children:
                return

            curr = curr.children[ch]

            if curr.isWord:
                res = True
                curr.isWord = False
            
            board[i][j] = "#"

            dfs(i+1,j,curr)
            dfs(i-1,j,curr)
            dfs(i,j+1,curr)
            dfs(i,j-1,curr)

            board[i][j] = ch
        
        for i in range(row):
            for j in range(col):
                dfs(i,j,root)
        return res