class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=defaultdict(list)
        for w in strs:
            hm["".join(sorted(w))].append(w)
        return list(hm.values())