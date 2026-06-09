class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count=defaultdict(int)
        for c in magazine:
            letter_count[c]+=1
        for c in ransomNote:
            if c not in letter_count:
                return False
            else:
                letter_count[c]-=1
                if letter_count[c]<0:
                    return False
        return True