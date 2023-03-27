class Solution:
    def bitwiseComplement(self, n: int) -> int:
        ans=bin(n)[2:]
        strn=''
        for i in ans:
            if i=="1":
                strn+="0"
            else:
                strn+="1"
        return int(strn,2)
