class Solution:
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(start):
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start, len(s)):
                substring = s[start:end + 1]

                if self.isPalindrome(substring):
                    path.append(substring)
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return res