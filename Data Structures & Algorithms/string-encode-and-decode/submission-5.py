class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==1:
            if strs[0]=="":
                return "."
        elif len(strs)==0:
            return ""
        return "-".join(strs)
    def decode(self, s: str) -> List[str]:
        if len(s)==1:
            if s==".":
                return [""]
        elif len(s)==0:
            return []
        return s.split("-")