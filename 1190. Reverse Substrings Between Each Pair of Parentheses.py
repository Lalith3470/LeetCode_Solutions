class Solution:
    def reverseParentheses(self, s: str) -> str:
        i=0
        stack=[]
        while i < len(s):
            if  s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                st = ''
                while stack and stack[-1]!='(': 
                    st += stack.pop() 
                stack.pop()
                stack += list(st)
            else:
                stack.append(s[i])
            i += 1
        return ''.join(stack)
