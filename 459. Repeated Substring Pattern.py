class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==1 or len(s)==len(set(s))==2:return False
        st=""
        for i in range(len(s)//2+1):
            st+=s[i]
            if st*(len(s)//(i+1))==s:
                return True
        else:
            return False
