class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) in [0,1]:
            return len(nums)
        arr=sorted(nums)
        j=0
        s=set()
        max=1
        for i in range(1,len(arr)):
            curr=arr[j]
            next=arr[i]
            s.add(curr)
            if abs(curr-next)!=1 and abs(curr-next)!=0:
                j=i
                l=len(s)
                if l>max:
                    max=l
                s.clear()
                continue
            s.add(next)
            j+=1
            l=len(s)
            if l>max:
                max=l
        return max