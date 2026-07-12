class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=b=0
        m=[]
        while a<len(nums1) and b<len(nums2):
            if nums1[a]<=nums2[b]:
                m.append(nums1[a])
                a+=1
            else:
                m.append(nums2[b])
                b+=1
        while a<len(nums1):
            m.append(nums1[a])
            a+=1
        while b<len(nums2):
            m.append(nums2[b])
            b+=1
        c=len(m)
        print(m)
        if c&1:
            return m[(c)//2]
        else:
            return (m[c//2]+m[c//2 - 1])/2