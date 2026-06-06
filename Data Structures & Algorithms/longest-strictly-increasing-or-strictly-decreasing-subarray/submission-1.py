class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        i,j=0,1
        inc,k=1,1
        while j<len(nums):
            print(f"i={i},j={j},{nums[i],nums[j]},inc={inc}")
            if nums[j]>nums[i]:
                k+=1
                i+=1
                j+=1
                inc=max(inc,k)
                continue
            k=1
            i+=1
            j+=1
        p,q=0,1
        dec,l=1,1
        while q<len(nums):
            print(f"p={p},q={q},{nums[p],nums[q]},dec={dec}")
            if nums[q]<nums[p]:
                l+=1
                p+=1
                q+=1
                dec=max(dec,l)
                continue
            l=1
            p+=1
            q+=1
        return max(inc,dec)