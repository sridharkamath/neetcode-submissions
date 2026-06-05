class Solution:
    def maxDifference(self, s: str) -> int:
        hm=defaultdict(int)
        for c in s:
            hm[c]+=1
        max_odd=0
        min_even=99
        for c,n in hm.items():
            if n%2==0 and n<min_even:
                min_even=n
            elif n%2!=0 and n>max_odd:
                max_odd=n
        return max_odd-min_even