class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        l1=len(s1)
        c1=Counter(s1)
        c2=Counter(s2[l:l1])
        for r in range(l1,len(s2)):
            print(c2)
            if c1==c2:
                return True
            else:
                c2[s2[r]]+=1
                c2[s2[l]]-=1
                if c2[s2[l]]==0:
                    del c2[s2[l]]
                l+=1
        return c1==c2