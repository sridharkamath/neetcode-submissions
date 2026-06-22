class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=Counter(chars)
        yes=0
        sum=0
        for w in words:
            temp=Counter(w)
            for ch in temp:
                if ch not in c:
                    yes=0
                    break
                elif temp[ch]>c[ch]:
                    yes=0
                    break
                yes=1
            if yes:
                sum+=len(w)
        return sum