class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s="+-*/"
        stack=[]
        for i in tokens:
            if i in s:
                val=eval(stack[-2]+i+stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(int(val)))
            else:
                stack.append(i)
        return int(stack[0])
