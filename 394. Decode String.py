class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack,n=[],"" 
        for i in s: 
            if i.isdigit(): 
                n+=i 
            elif i=="[": 
                stack.append(n) 
                n='' 
            elif i.isalpha(): 
                stack.append(i)
            if i=="]": 
                st=[]
                while stack: 
                    val=stack.pop()
                    if val.isdigit(): 
                        stack.append(''.join(st[::-1]*int(val)))
                        break
                    else:
                        st.append(val)
        return ''.join(stack) 
