class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt=0
        stack=[]
        for i in range(len(s)):
            if(s[i]=="(" and cnt!=0):
                stack.append(s[i])
                cnt+=1
            elif(s[i]==")" and cnt!=1):
                stack.append(s[i])
                cnt-=1
            elif(s[i]=="(" and cnt==0):
                cnt+=1
            else:
                cnt-=1
        return "".join(stack)
