class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        for i,h in enumerate(heights):
            j=i+1
            width=1
            while j<len(heights):
                if h<=heights[j]:
                    width+=1
                else:
                    break
                j+=1
            k=i-1
            while k>-1:
                if h<=heights[k]:
                    width+=1
                else:
                    break
                k-=1
            curr_area=h*width
            res=max(curr_area,res)
        return res     