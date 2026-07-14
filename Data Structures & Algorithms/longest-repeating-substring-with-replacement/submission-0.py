class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        m=defaultdict(int)
        res=0
        for r in range(len(s)):
            m[s[r]]+=1
            mfc,mf=max(m),max(m.values())
            while (len(s[l:r+1])-mf)>k:
                m[s[l]]-=1
                if m[s[l]]==0:
                    del m[s[l]]
                l+=1
            res=max(res,r-l+1)
        return res

