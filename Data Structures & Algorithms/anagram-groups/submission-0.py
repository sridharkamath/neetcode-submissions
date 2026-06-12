class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=defaultdict(list)
        for i in range(len(strs)):
            s=str(sorted(strs[i]))
            hm[s].append(strs[i])
        return list(hm.values())
        

            
        
        

