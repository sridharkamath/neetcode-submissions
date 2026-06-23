class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        ans=[]
        for n,m in c.items():
            ans.append((m,n))
        ans=sorted(ans)
        return [n for _,n in ans[-k:]]