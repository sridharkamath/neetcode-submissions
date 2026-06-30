class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                a=num.pop()
                b=num.pop()
                num.append(a+b)
            elif tokens[i]=="-":
                b=num.pop()
                a=num.pop()
                num.append(a-b)
            elif tokens[i]=="*":
                a=num.pop()
                b=num.pop()
                num.append(a*b)
            elif tokens[i]=="/":
                b=num.pop()
                a=num.pop()
                num.append(int(a/b))
            else:
                num.append(int(tokens[i]))
        return num.pop()