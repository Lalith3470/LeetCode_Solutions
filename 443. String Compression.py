class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        stack=[]
        lst=[]
        for i in chars:
            if stack and stack[-1]!=i:
                lst.append(stack[-1])
                if len(stack)!=1:
                    ln=str(len(stack))
                    for num in ln:
                        lst.append(num)
                stack=[]
                stack.append(i)
            else:
                stack.append(i)
        lst.append(stack[-1])
        if len(stack)!=1:
            ln=str(len(stack))
            for num in ln:
                lst.append(num)
        chars[:]=lst
