class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        else:
            curr_l_index=0
            freq_l_s={}
            freq_l_t={}
            for c in s:
                if c not in freq_l_s:
                    freq_l_s[c]=1
                else:
                    freq_l_s[c]+=1
            for c in t:
                if c not in freq_l_t:
                    freq_l_t[c]=1
                else:
                    freq_l_t[c]+=1
            for l,f in freq_l_s.items():
                if f > freq_l_t.get(l,0): 
                    print("failing 1")   
                    return False
            else:
                for l in s:
                    if l not in t:
                        print("failing 2")
                        return False
                    for i,c in enumerate(t):
                        if l==c and i<len(t):
                            t=t[i:]
                            break
                        elif l!=c and i<len(t):
                            continue
                        else:
                            print("failing 3")
                            return False
                return True

