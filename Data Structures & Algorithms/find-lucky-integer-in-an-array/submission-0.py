class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm=defaultdict(int)
        for n in arr:
            hm[n]+=1
        l=-1
        for n in hm:
            if hm[n]==n and n>l:
                l=n
        return l