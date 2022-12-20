class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        rev_str=''
        for i in reversed(range(len(s))):
            if i==0:rev_str+=s[i]
            else:rev_str+=s[i]+' '
                
        return rev_str
