class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n=bin(n)[2:]
        stack=[]
        stack.append(n[0])
        for i in range(1,len(n)):
            if n[i]=="1" and stack[-1]!="1":
                stack.append(n[i])
            elif n[i]=="0" and stack[-1]!="0":
                stack.append(n[i])
            else:
                return False
        return True
