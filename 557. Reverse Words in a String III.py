class Solution:
    def reverseWords(self, s: str) -> str:
        st=''
        s=s.split()
        for i in range(len(s)):
            a=s[i]
            st+=a[::-1]
            if i<len(s)-1:
                st+=' '
                
        return st
