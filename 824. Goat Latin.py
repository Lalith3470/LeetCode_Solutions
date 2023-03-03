class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        eql="aeiouAEIOU"
        s = sentence.split()
        res=''
        for i in range(len(s)):
            if s[i][0] in eql:
                res+=s[i]+"ma"
            else:
                res+=s[i][1:]+s[i][0]+"ma"
            res+="a"*(i+1)+" "
        return res.strip()
