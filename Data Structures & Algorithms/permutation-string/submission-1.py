class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        l1=len(s1)
        c1=Counter(s1)
        for r in range(l1,len(s2)+1):
            c2=Counter(s2[l:r])
            print(c2)
            if c1==c2:
                return True
            else:
                l+=1
        return False