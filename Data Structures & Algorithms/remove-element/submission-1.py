class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        while val in nums:
            nums.remove(val)
            nums.append("_")
            k+=1
        return len(nums)-k