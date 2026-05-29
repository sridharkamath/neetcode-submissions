class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        chars=""
        for i in range(len(strs[0])):
            char=strs[0][i]
            print(chars, char)
            for word in strs[1:]:
                if char in word[i:]:
                    continue
                else:
                    return chars
            chars+=strs[0][i]
        return chars
            