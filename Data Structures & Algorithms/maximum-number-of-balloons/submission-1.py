class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm={"b":0,"a":0,"l":0,"o":0,"n":0}
        for c in text:
            if c in hm:
                hm[c]+=1
        
        hm["l"]=hm["l"]//2
        hm["o"]=hm["o"]//2

        return min(hm.values())