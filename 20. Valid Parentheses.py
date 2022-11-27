class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        lst=["(","{","["]
        for i in s:
            if i in lst:
                stack.append(i)
            if stack and i=='}' and stack[-1]=="{":
                stack.pop()
            elif stack and i==']'and stack[-1]=="[":
                stack.pop()
            elif stack and i==')'and stack[-1]=="(":
                stack.pop()
            elif i==")" or i=="}" or i=="]":
                stack.append(i)
        return len(stack)==0
