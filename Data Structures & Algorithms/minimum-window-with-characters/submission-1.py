class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        else:
            l=0

            l1=len(s)
            l2=len(t)

            c1=defaultdict(int)
            c2=Counter(t)

            res=""
            m=9999

            have=0
            need=len(c2)

            for r in range(l1):

                if s[r] in c2:
                    c1[s[r]]+=1
                    if c1[s[r]] == c2[s[r]]:
                        have+=1
                    
                while have==need:
                    if (r-l+1)<m:
                        res=s[l:r+1]
                        m=r-l+1
                    if s[l] in c2:
                        c1[s[l]]-=1
                        if c1[s[l]] < c2[s[l]]:
                            have-=1
                        if c1[s[l]]==0:
                            del c1[s[l]]
                    l+=1
            return res