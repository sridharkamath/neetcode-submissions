class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s=set()
        for email in emails:
            ln,dn=email.split("@")
            if "+" in ln:
                ln,*_=ln.split("+")
            if "." in ln:
                ln="".join(ln.split("."))
            email=ln+dn
            s.add(email)
        return len(s)
