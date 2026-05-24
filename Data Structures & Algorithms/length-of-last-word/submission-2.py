class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i,j,l=0,0,0
        while j<len(s):
            if s[j]==" " and s[i]!=" ":
                l=(j-1)-i+1
                i=j+1
            elif j==len(s)-1 and s[j]!=" ":
                l=j-i+1
                i=j+1
            elif s[j]==" " and s[i]==" ":
                i=j+1
            j+=1
        return l