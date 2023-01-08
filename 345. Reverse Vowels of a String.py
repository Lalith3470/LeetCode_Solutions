class Solution:
    def reverseVowels(self, s: str) -> str:
        a='aeiouAEIOU'
        b=''
        for i in s:
            word=set(i)
            if word.issubset(a):
                b+=i
        b=b[::-1]
        c=''
        l=0
        for i in s:
            word=set(i)
            if word.issubset(a):
                c+=b[l]
                l+=1
            else:
                c+=i
        return c
