class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hm=Counter(nums)
        good_pairs=0
        for _,v in hm.items():
            if v>1:
                good_pairs+= (v*(v-1))//2
        return good_pairs