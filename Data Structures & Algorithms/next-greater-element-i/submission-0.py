class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm={}
        hm[nums2[-1]]=-1
        for i in range(len(nums2)-1):
            m=nums2[i]
            for n in nums2[i+1:]:
                if n>m:
                    hm[m]=n
                    m=n
                    break
            if m==nums2[i]:
                hm[m]=-1
        ans=[]
        for j in nums1:
            ans.append(hm[j])
        return ans