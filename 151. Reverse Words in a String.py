class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        a=''
        for i in reversed(range(len(s))):
            if i==0:
                a+=s[i]
            else:
                a+=s[i]+' '
        return a
