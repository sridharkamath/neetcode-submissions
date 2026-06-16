class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ps={}
        sp={}
        s=s.split(" ")
        if len(s)!=len(pattern):
            return False
        else:
            for i in range(len(s)):
                print(list(ps),list(sp))
                if s[i] in sp:
                    if sp[s[i]]!=pattern[i]:
                        return False
                if pattern[i] in ps: 
                    if ps[pattern[i]]!=s[i]:
                        return False
                else:
                    sp[s[i]]=pattern[i]
                    ps[pattern[i]]=s[i]
        return True                