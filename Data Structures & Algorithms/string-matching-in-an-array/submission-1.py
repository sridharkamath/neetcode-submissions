class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for word in words:
            new=list(filter(lambda w: w!=word,words))
            for nw in new:
                if word in nw:
                    if word not in ans:
                        ans.append(word)
        return ans