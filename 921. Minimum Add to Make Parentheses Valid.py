class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        for i in s:
            if i=="(":
                stack.append(i)
            if i==")":
                if "(" in stack:
                    stack.remove("(")
                else:
                    stack.append(i) 
        return len(stack)
