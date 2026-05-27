class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        i=j=count=0
        while i<n and j<m:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                i+=1
        while j<m:
            j+=1
            count+=1
            
        return count