class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp=sorted(heights)
        n=0
        for i in range(len(heights)):
            if temp[i]!=heights[i]:
                n+=1
        return n