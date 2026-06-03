class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        elif len(set(s))!=len(set(t)):
            return False
        else:
            m={}
            for i in range(len(t)):
                if s[i] not in m:
                    s=s.replace(s[i],t[i])
                    m[s[i]]=t[i]
            return s==t   
