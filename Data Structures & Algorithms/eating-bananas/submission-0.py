import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        ans=r
        total=sum(piles)
        while l<=r:
            mid = l + ((r-l)//2)
            total_time=0
            for p in piles:
                total_time+=math.ceil(p/mid)
            if total_time>h:
                l=mid+1
            else:
                ans=mid
                r=mid-1
        return ans