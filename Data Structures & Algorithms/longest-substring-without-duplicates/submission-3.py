class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        curr_char = set()
        l = 0

        for r in range(len(s)):
            while s[r] in curr_char:
                curr_char.remove(s[l])
                l += 1

            curr_char.add(s[r])
            res = max(res, r - l + 1)

        return res