class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        a=''
        for i in s:
            if i.isalpha():
                a+=i
        l=a[::-1]
        c=0
        b=''
        for i in range(len(s)):
            if s[i].isalpha():
                b+=l[c]
                c+=1
            else:
                b+=s[i]
        return b
