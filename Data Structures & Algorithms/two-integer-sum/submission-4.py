class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[[num,i] for i,num in enumerate(nums)]
        a.sort()
        i,j=0,len(a)-1
        while i!=j:
            if a[i][0]+a[j][0]==target: break
            if a[i][0]+a[j][0]>target: j-=1
            if a[i][0]+a[j][0]<target: i+=1
        return [min(a[i][1],a[j][1]),max(a[i][1],a[j][1])]