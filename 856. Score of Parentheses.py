class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        cnt = 0
        for c in s :
            if c=="(":
                stack.append(cnt)
                cnt=0
            else:
                a=stack.pop()
                cnt=a+max(1,cnt*2) 
        return cnt
