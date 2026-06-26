class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl=s.lower()
        l,r=0,len(s)-1
        while l<r:
            if not sl[l].isalnum():
                l+=1
                continue
            if not sl[r].isalnum():
                r-=1
                continue
            if sl[l]!=sl[r]:
                return False
            l+=1
            r-=1
        return True