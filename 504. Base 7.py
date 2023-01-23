class Solution:
    def convertToBase7(self, num: int) -> str:
        if num ==0:
            return "0"
        string = ""
        s = abs(num)
        while s:
            string+=str(s%7)
            s//=7
        if num<0:
            return "-"+string[::-1]
        else:
            return string[::-1]
