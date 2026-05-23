class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            sf={}
            tf={}
            for l in s:
                if l in sf:
                    sf[l]+=1
                else:
                    sf[l]=1
            for l in t:
                if l in tf:
                    tf[l]+=1
                else:
                    tf[l]=1
            print(sf, tf)
            if sf == tf: return True
        return False