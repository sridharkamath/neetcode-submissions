class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)&1:
            return False
        else:
            n=len(s)
            m={"(":")","{":"}","[":"]"}
            b=[]
            oc=cc=0
            for c in s:
                if c in "({[":
                    b.append(c)
                    oc+=1
                else:
                    if not b:
                        return False
                    o=b.pop()
                    if c!=m[o]:
                        return False
                    cc+=1
            if oc!=cc:
                return False
            return True