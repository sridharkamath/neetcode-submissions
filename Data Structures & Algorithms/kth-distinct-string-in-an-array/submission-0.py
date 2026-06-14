class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s=defaultdict(int)
        for e in arr:
            if e in s:
                s[e]+=1
            else:
                s[e]=1
        i=0
        if len(list(s))>=k:
            for key in s:
                if s[key]==1:
                    i+=1
                    if i==k:
                        return key
        return ""